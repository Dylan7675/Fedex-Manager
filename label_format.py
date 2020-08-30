import pandas as pd
import usaddress

"""
TODO: Change reading a specific csv to reading a file path from fileDialog
Example: Make this script a callable function from main.app taking path as input
"""

dataset = pd.read_csv('fedex_upload.csv',
          names=["Name","Invoice","Address","Phone"])

# Dictionary keys from usaddress module
address1_keys = ['AddressNumber', 'StreetNamePreDirectional', 'StreetName',
                 'StreetNamePostType', 'StreetNamePostDirectional']
address2_keys = ['OccupancyType', 'OccupancyIdentifier']

# Package Constants
weight = 3
country = "US"
signature = 4 # ASR = 4

fedex_df = pd.DataFrame(columns=["FullName","Address1","Address2",
                                 "City","State","Zip","Phone","CountryCode",
                                 "Weight", "Invoice", "Signature"])

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
    for k in address1_keys:
        if k in parsed_address.keys():
            address1 = " ".join([address1, parsed_address[k]])

    # Combining address2 OccupancyType and OccupancyIdentifier
    for k in address2_keys:
        if k in parsed_address.keys():
            address2 = " ".join([address2, parsed_address[k]])

    # Validate user submitted city, state, and zip
    try:
        city = parsed_address['PlaceName']
    except KeyError:
        city = "VALIDATE CITY"
        print(f"Validate the City of {name}")
    try:
        state = parsed_address['StateName']
    except KeyError:
        state = "VALIDATE STATE"
        print(f"Validate the State of {name}")
    try:
        zip_code = parsed_address['ZipCode']
    except KeyError:
        zip_code = "VALIDATE ZIP"
        print(f"Validate the Zip of {name}")

    # Structure data into new df row
    new_row = {
               "FullName": name,
               "Address1": address1,
               "Address2": address2,
               "City": city,
               "State": state,
               "Zip": zip_code,
               "Phone": phone,
               "CountryCode": country,
               "Weight": weight,
               "Invoice": invoice,
               "Signature": signature
              }

    fedex_df = fedex_df.append(new_row, ignore_index=True)
    #fedex_df.to_csv("fedex_bulk_print.csv", index=False)



if __name__ == '__main__':
    main()
