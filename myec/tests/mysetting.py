import unittest

from common.common import connect_and_send_requests
from myec.business_common.Utility import HEADER1, HEADER2, ServiceURLs, ServiceRequestMethod


class MySettingPageCheck(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_setting_page_check(self, username='stest12798', password=1):
        body1 = {
            "serviceRequest": {
                "header": HEADER1,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        result = connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body1)
        token = result[0]
        sessionId = result[1]

        body2 = {
            "serviceRequest": {
                "header": HEADER2,
                "body": {
                    "countrycode": "CN",
                    "partnercode": "Cool",
                    "token": token,
                    "sessionId": sessionId,
                    "siteversion": "development",
                    "dataStore": "us1"
                }
            }
        }
        print body2
        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.MY_SETTING_SERVICE_URL, body2)

if __name__ == '__main__':
    unittest.main()