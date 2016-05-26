import unittest
from common.common import connect_and_send_requests
from myec.business_common.Utility import HEADER, ServiceURLs, ServiceRequestMethod


class LoginRelated(unittest.TestCase):

    def setUp(self):
        pass

    def test_with_valid_username_and_password(self, username='stest12787', password='1'):
        body = {
            "serviceRequest": {
                "header": HEADER,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body)

    def test_login_with_other_partner_account(self, username='stest12116', password='1'):
        body = {
            "serviceRequest": {
                "header": HEADER,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()