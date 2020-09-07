import pandas as pd
import usaddress
from states import US_states
import re

"""
TODO: Change reading a specific csv to reading a file path from fileDialog
Example: Make this script a callable function from main.app taking path as input
"""


class Formatter:

    def __init__(self, csv_path):

        self.csv_path = csv_path

        # Dictionary keys from usaddress module
        self.address1_keys = ['AddressNumber', 'StreetNamePreDirectional', 'StreetName',
                              'StreetNamePostType', 'StreetNamePostDirectional']

        self.address2_keys = ['OccupancyType', 'OccupancyIdentifier']

        # Package Constants
        self.weight = 3
        self.country = "US"
        self.signature = 4  # ASR = 4

        self.logs = []

        self.fedex_df = pd.DataFrame(columns=["FullName", "Address1", "Address2",
                                         "City", "State", "Zip", "Phone", "CountryCode",
                                         "Weight", "Invoice", "Signature"])

    def parse_csv(self):
        """
        :param csv_path:
        :return: fedex_df
        """

        dataset = pd.read_csv(self.csv_path, names=["Name", "Invoice", "Address", "Phone"])

        # Iterate over rows of user submissions
        for ind in dataset.index:

            address1 = ""
            address2 = ""

            name = dataset['Name'][ind]
            full_address = dataset['Address'][ind]
            phone = dataset['Phone'][ind]
            invoice = dataset['Invoice'][ind]

            # Parsed address into a dictionary
            parsed_address = usaddress.tag(full_address)[0]

            # Combining address1, pre, and post identifiers
            for k in self.address1_keys:
                if k in parsed_address.keys():
                    address1 = " ".join([address1, parsed_address[k]])

            # Address should never be left blank
            if not address1:
                self.logs.append(f"Validate the Address of {name}\n\n")

            # Combining address2 OccupancyType and OccupancyIdentifier
            for k in self.address2_keys:
                if k in parsed_address.keys():
                    address2 = " ".join([address2, parsed_address[k]])

            # Validate user submitted city, state, and zip
            try:
                city = " ".join([name.capitalize() for name in
                                 parsed_address['PlaceName'].split()])
            except KeyError:
                city = "VALIDATE CITY"
                self.logs.append(f"Validate the City of {name}\n\n")

            try:

                state = " ".join([name.capitalize() for name in
                                  parsed_address['StateName'].split()])

                # Regex validate special characters from State
                state = state_validator(state)

                state = US_states[state].upper()

            except KeyError:
                state = "VALIDATE STATE"
                self.logs.append(f"Validate the State of {name}\n\n")

            try:
                zip_code = parsed_address['ZipCode']
            except KeyError:
                zip_code = "VALIDATE ZIP"
                self.logs.append(f"Validate the Zip of {name}\n\n")

            # Structure data into new df row
            new_row = {
                       "FullName": name,
                       "Address1": address1,
                       "Address2": address2,
                       "City": city,
                       "State": state.upper(),
                       "Zip": zip_code,
                       "Phone": phone,
                       "CountryCode": self.country,
                       "Weight": self.weight,
                       "Invoice": invoice,
                       "Signature": self.signature
                      }

            self.fedex_df = self.fedex_df.append(new_row, ignore_index=True)

        return self.fedex_df


def state_validator(state_name):
    """ Removes any special characters from state name """

    if not re.match('^[a-zA-Z_ ]+$', state_name):
        for char in state_name:
            if not re.match('^[a-zA-Z_ ]+$', char):
                fixed_state = state_name.replace(char, "")
        return fixed_state
    return state_name


if __name__ == '__main__':
    main()
