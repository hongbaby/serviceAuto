# coding: utf-8

import os
import csv
import httplib
from urlparse import urlparse
import requests
import json
from myec.business_common.Utility import JSONResponse, ServiceRequestMethod


def connect_and_send_requests(method, url_str, body):
    url = urlparse(url_str)
    hostname = url.hostname
    try:
        httplib.HTTPConnection(hostname)
    except Exception, e:
        print "Http connection issue: %s" % e
    return send_requests(method, url_str, body)


def send_requests(method=ServiceRequestMethod.POST, url='', body={}):
    if method == ServiceRequestMethod.POST:
        request = requests.post(url, json=body)
        response_status_code = request.status_code
        if response_status_code == 200:
            response_string = request.content
            json_response = json.loads(response_string)
            error_code = get_error_code_from_response_header(json_response)
            print error_code
            if error_code == 0:
                print "json_response: "
                print json_response
                if url.endswith('login'):
                    token, session_id = get_token_and_session_id_after_login(json_response)
                    print token
                    print session_id
                    return token, session_id
        else:
            print "The response status code is: %d" % response_status_code
            print request.reason


# def get_error_code_and_description(dic={}):
#     if isinstance(dic, dict):
#         for key, value in dic.iteritems():
#             if key == JSONResponse.HEADER:
#                 print "key_name is: %s, value is: %s" % (key, value)
#                 compare_error_code_and_error_description(value)
#             if isinstance(dic[key], dict):
#                 get_error_code_and_description(dic[key])


def get_token_and_session_id_after_login(json_response={}):
    if isinstance(json_response, dict):
        if JSONResponse.SERVICE_RESPONSE in json_response.keys():
            response_value = json_response[JSONResponse.SERVICE_RESPONSE]
            if JSONResponse.BODY in response_value.keys():
                body_value = response_value[JSONResponse.BODY]
                if JSONResponse.LOGIN_RESULT in body_value.keys():
                    token = get_value_from_dict(body_value[JSONResponse.LOGIN_RESULT], JSONResponse.TOKEN)
                    session_id = get_value_from_dict(body_value[JSONResponse.LOGIN_RESULT], JSONResponse.SESSION_ID)
                    return token, session_id


def get_value_from_dict(dic={}, key_name=''):
    for k, v in dic.iteritems():
        if k == key_name:
            return v


def get_error_code_from_response_header(dic={}):
    if isinstance(dic, dict):
        if JSONResponse.SERVICE_RESPONSE in dic.keys():
            response_value = dic[JSONResponse.SERVICE_RESPONSE]
            if isinstance(response_value, dict) and JSONResponse.HEADER in response_value.keys():
                error_value = response_value[JSONResponse.HEADER]
                print error_value
                return compare_error_code_and_error_description(error_value)


def compare_error_code_and_error_description(dic={}):
    if JSONResponse.ERRORCODE in dic.keys():
        error_code = dic[JSONResponse.ERRORCODE]
        if error_code != 0:
            err_description = dic[JSONResponse.ERROR_DESCRIPTION]
            verify_error_description(error_code, err_description)
        return error_code
    else:
        print "Cannot find %s in dic" % JSONResponse.ERRORCODE
        return


def verify_error_description(error_code, error_description):
    current_path = os.getcwd()
    thePath = current_path[:current_path.find("serviceAuto\\") + len("serviceAuto") + 1]

    with open(os.path.dirname(thePath) + "\myec\data\error_code.csv", 'r') as csvfile:
        csvfile.readline()
        reader = csv.reader(csvfile)
        for code, description in reader:
            if int(code) == int(error_code):
                try:
                    assert error_description == description
                except AssertionError:
                    print "Assertion error: the expected error_description is: %s; " \
                          "While the actual error description is: %s" % (description, error_description)
                break


def get_specfic_value_from_multiple_nest_dict(dic={}, key_name=''):
    if isinstance(dic, dict):
        for k in dic.iterkeys():
            if k == key_name:
                print key_name
                return key_name
            else:
                if isinstance(dic[k], dict):
                    for i in dic[k].iterkeys():
                        if i == key_name:
                            print dic[k][i]
                            return key_name
                        else:
                            print dic[k][i]
                            return get_specfic_value_from_multiple_nest_dict(dic[k][i], key_name)

print get_specfic_value_from_multiple_nest_dict(dic={
    "serviceResponse": {
        "header": {
            "errorCode": 0,
            "errorDescription": "demo description",
            "lastUpdate": 12345678
        },
        "body": {
            "mySettings":

                    {
                        "name": "contacus",
                        "displayName": "Contact Us",
                        "targetData": "contactus"
                    }


        }
    }
}, key_name='displayName')