# Fedex-Manager
A simple program for creating batch shipping labels and tracking multiple shipments.

## Installation

```
git clone git@github.com:Dylan7675/Fedex-Manager.git
```

Change directories into the repository.

```
cd Fedex-Manager
```

Install the required dependencies:

````
pip install -r requirements.txt
````
**Important**: Depending on your system, make sure to use pip3 and python3 instead.

### Running

From the repository, run app.py

```
python app.py
```

If you run into any issues with not having pyqt installed on your system.... please run:

For Linux
```
sudo apt-get install python3-pyqt5 
```

For MacOS
```
brew install pyqt
```

## Shipping Tools
This section will cover how to use the available tools within this program. Currently there are two ways to create batch shipping labels within the program. You can either export the processed recipient data as a csv file or directly preparing the labels via the Fedex API and printing them to a USB printer.(Fedex API configuration credentials required. Directions listed below.)

### Tracking

To use the tracking functionality, paste your list of tracking numbers either space(enter) or comma(,) seperated in the Tracking Numbers box. Press the "Track Shipments" button and it will begin processing your request. Once it completes tracking your shipments, it will update the table to the right with the tracking statuses. You are able to copy the data directly out of this table. Please note, the speed of the tracking request is determined by the quantity of tracking numbers submitted.

<img src="https://imgur.com/JInTUXO.png">

### Batch Labels
As mentioned earlier, there are currently two methods to prepare batch labels. Batch labels can be prepared either via Exporting a csv file to be uploaded to Fedex ShipManager or by directly creating and printing the labels via the Fedex API. If you would like to create labels via the API, account credentials will need to be loaded into the tool.(Directions below.) Either way you decide, both methods start with the same process.

First start by preparing a csv file with the following data(no headers):

- Col1: Recipient Name
- Col2: Invoice Number
- Col3: Recipient Address
- Col4: Recipient Phone Number

<img src="https://imgur.com/bYKTNMt.png">

Once the csv has been prepared, use the "Browse" button to open the file and Parse the recipient addresses. After the addresses have been parsed, the recipient table will be updated. You can make edits in the table in case of minor errors while parsing.

After your recipient data has been confirmed, you can proceed to export the table as a csv or directly print with a USB Label Printer(In my case, a Zebra label printer).

<img src="https://imgur.com/TDarkHh.png">

### Configuration Loader
The Configuration loader is used to create a shipper profile with your Shipper Address and Fedex API credentials. For further steps enabling API access for you account, please visit https://www.fedex.com/en-us/developer/web-services.html

To access the config loader, there is a config tool listed on the toolbar for this program.

#### New Config
To create a new config, select Config > New Config. Complete all fields to submit your Shipper Address and Account Credentials. Save the new configuration you have just created. It will check your connection to Fedex to confirm your account credentials are accurate.

<img src="https://imgur.com/pxtg2i6.png">

#### Load Config
You can load a configuration for a shipper config you have already created. Config > Load Config will have a list of available configs you can select from.
