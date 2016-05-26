import httplib
from urlparse import urlparse
import requests
import json
from myec.business_common.Utility import JSONResponse, ServiceRequestMethod


def send_requests(method=ServiceRequestMethod.POST, url='', body={}):
    if method == ServiceRequestMethod.POST:
        request = requests.post(url, json=body)
        response_status_code = request.status_code
        if response_status_code == 200:
            response_string = request.content
            json_response = json.loads(response_string)
            print json_response
            get_error_code_and_description(json_response)
        else:
            print "The response status code is: %d" % response_status_code
            print request.reason


def connect_and_send_requests(method, url_str, body):
    url = urlparse(url_str)
    hostname = url.hostname
    try:
        httplib.HTTPConnection(hostname)
        send_requests(method, url_str, body)

    except Exception, e:
        print "Http connection issue: %s" % e


def get_error_code_and_description(dic={}):
    if isinstance(dic, dict):
        for key, value in dic.iteritems():
            if key == JSONResponse.HEADER:
                print "key_name is: %s, value is: %s" % (key, value)
            if isinstance(dic[key], dict):
                get_error_code_and_description(dic[key])

