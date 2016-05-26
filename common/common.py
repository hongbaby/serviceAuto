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
    send_requests(method, url_str, body)


def send_requests(method=ServiceRequestMethod.POST, url='', body={}):
    if method == ServiceRequestMethod.POST:
        request = requests.post(url, json=body)
        response_status_code = request.status_code
        if response_status_code == 200:
            response_string = request.content
            json_response = json.loads(response_string)
            get_error_code_and_description(json_response)
        else:
            print "The response status code is: %d" % response_status_code
            print request.reason


def get_error_code_and_description(dic={}):
    if isinstance(dic, dict):
        for key, value in dic.iteritems():
            if key == JSONResponse.HEADER:
                print "key_name is: %s, value is: %s" % (key, value)
                compare_error_code_and_error_description(value)
            if isinstance(dic[key], dict):
                get_error_code_and_description(dic[key])


def compare_error_code_and_error_description(dict):
    error_code = dict[JSONResponse.ERRORCODE]
    if error_code:
        err_description = dict[JSONResponse.ERROR_DESCRIPTION]
        verify_error_description(error_code, err_description)
    else:
        print "Login successfully."


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