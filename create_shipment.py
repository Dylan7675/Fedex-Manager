import fedex
from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from fedex.services.ship_service import FedexProcessShipmentRequest
import json
import datetime
import binascii
import sys
import serial
from typing import Dict

class Configuration:

    def __init__(self):

        with open("config.json") as f:
            config = json.load(f)

        self.CONFIG_OBJ = FedexConfig(key=config['Account']['key'],
                                 password=config['Account']['password'],
                                 account_number=config['Account']['number'],
                                 meter_number=config['Account']['meter'],
                                 use_test_server=True)

        self.shipper_data = config['Shipper']

class Shipment(Configuration):

    def __init__(self, recipient_data: Dict):

        Configuration.__init__(self)
        self.recipient_data = recipient_data
        self.GENERATE_IMAGE_TYPE = 'PDF'
        self.label_binary_data = None
        self.shipment = None
        self.track_id = None

    def tracker(self, tracking_number):

        track = FedexTrackRequest(self.CONFIG_OBJ)
        track.SelectionDetails.PackageIdentifier.Type = 'TRACKING_NUMBER_OR_DOORTAG'
        track.SelectionDetails.PackageIdentifier.Value = tracking_number
        track.send_request()
        print(track.response)

    def create_shipment(self):

        self.shipment = FedexProcessShipmentRequest(self.CONFIG_OBJ)

        self.shipment.RequestedShipment.DropoffType = 'REGULAR_PICKUP'
        self.shipment.RequestedShipment.ServiceType = 'PRIORITY_OVERNIGHT'
        self.shipment.RequestedShipment.PackagingType = 'YOUR_PACKAGING'

        self.shipment.RequestedShipment.Shipper.Contact.PersonName = \
                                                self.shipper_data['Name']

        self.shipment.RequestedShipment.Shipper.Contact.PhoneNumber = \
                                                self.shipper_data['Phone']

        self.shipment.RequestedShipment.Shipper.Address.StreetLines = \
                                                [self.shipper_data['Address1'],\
                                                self.shipper_data['Address2']]

        self.shipment.RequestedShipment.Shipper.Address.City = \
                                                self.shipper_data['City']

        self.shipment.RequestedShipment.Shipper.Address.StateOrProvinceCode = \
                                                self.shipper_data['State']

        self.shipment.RequestedShipment.Shipper.Address.PostalCode = \
                                                self.shipper_data['Zip']

        self.shipment.RequestedShipment.Shipper.Address.CountryCode = \
                                                self.shipper_data['Country']

        self.shipment.RequestedShipment.Recipient.Contact.PersonName = \
                                                self.recipient_data['FullName']

        self.shipment.RequestedShipment.Recipient.Contact.PhoneNumber = \
                                                self.recipient_data['Phone']

        self.shipment.RequestedShipment.Recipient.Address.StreetLines = \
                                                [self.recipient_data['Address1'],\
                                                self.recipient_data['Address2']]

        self.shipment.RequestedShipment.Recipient.Address.City = \
                                                self.recipient_data['City']

        self.shipment.RequestedShipment.Recipient.Address.StateOrProvinceCode = \
                                                self.recipient_data['State']

        self.shipment.RequestedShipment.Recipient.Address.PostalCode = \
                                                self.recipient_data['Zip']

        self.shipment.RequestedShipment.Recipient.Address.CountryCode = \
                                                self.recipient_data['Country']

        self.shipment.RequestedShipment.EdtRequestType = 'NONE'

        self.shipment.RequestedShipment.ShippingChargesPayment.Payor.ResponsibleParty.AccountNumber = \
                                                self.CONFIG_OBJ.account_number
        # self.shipment.RequestedShipment.ShipTimestamp = datetime.datetime.now().replace(microsecond=0).isoformat()

        self.shipment.RequestedShipment.ShippingChargesPayment.PaymentType = 'SENDER'

        self.shipment.RequestedShipment.LabelSpecification.LabelFormatType = 'COMMON2D'
        self.shipment.RequestedShipment.LabelSpecification.ImageType = \
                                                self.GENERATE_IMAGE_TYPE

        self.shipment.RequestedShipment.LabelSpecification.LabelStockType = 'PAPER_7X4.75'
        self.shipment.RequestedShipment.LabelSpecification.LabelPrintingOrientation = \
                                                'BOTTOM_EDGE_OF_TEXT_FIRST'

        # Use order if setting multiple labels or delete
        #del self.shipment.RequestedShipment.LabelSpecification.LabelOrder

        # Package Details
        package1_weight = self.shipment.create_wsdl_object_of_type('Weight')
        package1_weight.Value = self.recipient_data['Weight']
        package1_weight.Units = "LB"
        package1 = self.shipment.create_wsdl_object_of_type('RequestedPackageLineItem')
        package1.PhysicalPackaging = 'PACKAGE'
        package1.Weight = package1_weight

        # Cost Center
        customer_reference = self.shipment.create_wsdl_object_of_type('CustomerReference')
        customer_reference.CustomerReferenceType="CUSTOMER_REFERENCE"
        customer_reference.Value = self.shipper_data['CostCenter']
        package1.CustomerReferences.append(customer_reference)

        # Invoice number
        invoice_number = self.shipment.create_wsdl_object_of_type('CustomerReference')
        invoice_number.CustomerReferenceType="INVOICE_NUMBER"
        invoice_number.Value = self.recipient_data['Invoice']
        package1.CustomerReferences.append(invoice_number)

        # Signature
        package1.SpecialServicesRequested.SpecialServiceTypes = 'SIGNATURE_OPTION'
        package1.SpecialServicesRequested.SignatureOptionDetail.OptionType = 'ADULT'

        # Create Shipment
        self.shipment.add_package(package1)
        self.shipment.send_validation_request()
        self.shipment.send_request()

        assert self.shipment.response
        #print("HighestSeverity: {}".format(self.shipment.response.HighestSeverity))
        #assert self.shipment.response.HighestSeverity == 'SUCCESS'
        self.track_id = \
            self.shipment.response.CompletedShipmentDetail.CompletedPackageDetails[0].TrackingIds[0].TrackingNumber

        assert self.track_id

        print(f'{self.track_id} Created')

    def label_2pdf(self):

        # Making the label
        if self.shipment:

            ascii_label_data = self.shipment.response.CompletedShipmentDetail.CompletedPackageDetails[0].Label.Parts[0].Image
            self.label_binary_data = binascii.a2b_base64(ascii_label_data)

            # Writing label to pdf
            out_path = f'{self.track_id}.{self.GENERATE_IMAGE_TYPE.lower()}'
            with open(out_path, 'wb') as f:
                f.write(self.label_binary_data)

    def print_label(self):

        # Print Label to Serial Printer
        if self.label_binary_data:

            label_printer = serial.Serial(0)
            print("SELECTED SERIAL PORT: "+ label_printer.portstr)
            label_printer.write(self.label_binary_data)
            label_printer.close()


if __name__ == '__main__':
    main()
