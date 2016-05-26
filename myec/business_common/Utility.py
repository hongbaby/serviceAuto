SERVICE_ROOT = "http://smartuat2.englishtown.com/"
HEADER = {
            "productId": 3,
            "platform": "iOS",
            "appVersion": "1.0.0",
            "culturecode": "en"
         }


class JSONResponse:
    HEADER = "header"
    ERRORCODE = "errorCode"
    ERROR_DESCRIPTION = "errorDescription"


class ServiceURLs:
    LOGIN_SERVICE_URL = SERVICE_ROOT + "services/api/ecplatform/service/login"


class ServiceRequestMethod:
    GET = "GET"
    POST = "POST"