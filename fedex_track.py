import requests
import json
import sys

class Tracker:

    def track(self, tracking_number):
        """
        Input: Tracking Number
        Output: Returns tracking status
        """

        # Requests data from fedex per tracking number
        info = requests.post('https://www.fedex.com/trackingCal/track',
        data={
        'data': json.dumps({
            'TrackPackagesRequest': {
                'appType': 'wtrk',
                'uniqueKey': '',
                'processingParameters': {
                    'anonymousTransaction': True,
                    'clientId': 'WTRK',
                    'returnDetailedErrors': True,
                    'returnLocalizedDateTime': False
                },
                'trackingInfoList': [{
                    'trackNumberInfo': {
                        'trackingNumber': str(tracking_number),
                        'trackingQualifier': '',
                        'trackingCarrier': ''
                    }
                }]
            }
        }),
        'action': 'trackpackages',
        'locale': 'en_US',
        'format': 'json',
        'version': 99
        }).json()

        status = info['TrackPackagesResponse']['packageList'][0]['keyStatus']

        return status

if __name__ == '__main__':
    main()
