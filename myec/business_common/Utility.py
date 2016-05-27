SERVICE_ROOT = "http://smartuat2.englishtown.com/"
HEADER1 = {
            "productId": 3,
            "platform": "iOS",
            "appVersion": "1.0.0",
            "culturecode": "en"
         }

HEADER2 = {
    "productId": 3,
    "platform": "iOS",
    "appVersion": "0.9.5",
    "culturecode": "en",  # zh-CN or en
    "lastUpdate": 0
}

class JSONResponse:
    SERVICE_RESPONSE = "serviceResponse"
    HEADER = "header"
    BODY = "body"
    LOGIN_RESULT = "loginResult"
    ERRORCODE = "errorCode"
    ERROR_DESCRIPTION = "errorDescription"
    TOKEN = "token"
    SESSION_ID = "sessionId"


class ServiceURLs:
    LOGIN_SERVICE_URL = SERVICE_ROOT + "services/api/ecplatform/service/login"
    MY_SETTING_SERVICE_URL = SERVICE_ROOT + "services/api/ecplatform/service/mysetting"


class ServiceRequestMethod:
    GET = "GET"
    POST = "POST"