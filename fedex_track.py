import requests
import json
import sys

class Tracker:
    """
    Tracker instanciates with a list of tracking numbers.
    """

    def __init__(self, tracking_list = []):
        self.tracking_list = tracking_list


    def track(self):
        """
        Input: tracking_list of Tracker instance
        Output: Returns a list of tracking statuses in order of input
        """

        tracked_list = []

        for tracking_number in self.tracking_list:

            #
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
            tracked_list.append(status)

        return tracked_list
            #print(f'{tracking_number}-{status}')

if __name__ == '__main__':
    main()
