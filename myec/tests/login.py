import unittest
from common.common import connect_and_send_requests
from myec.business_common.Utility import HEADER1, ServiceURLs, ServiceRequestMethod


class LoginRelated(unittest.TestCase):

    def setUp(self):
        pass

    def test_login_with_expired_account(self, username='stest12787', password='1'):
        body = {
            "serviceRequest": {
                "header": HEADER1,
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
                "header": HEADER1,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body)

    def test_login_with_invalid_account(self, username='stest12116', password='5'):
        body = {
            "serviceRequest": {
                "header": HEADER1,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body)

    def test_login_with_valid_account(self, username='stest12798', password='1'):
        body = {
            "serviceRequest": {
                "header": HEADER1,
                "body": {
                    "userName": username,
                    "password": password
                }
            }
        }

        connect_and_send_requests(ServiceRequestMethod.POST, ServiceURLs.LOGIN_SERVICE_URL, body)

    def tearDown(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LoginRelated("test_login_with_expired_account"))
    suite.addTest(LoginRelated("test_login_with_other_partner_account"))
    suite.addTest(LoginRelated("test_login_with_invalid_account"))
    suite.addTest(LoginRelated("test_login_with_valid_account"))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())