#!/usr/bin/python

import sys
import json
import urllib2
import collections

url = "http://192.168.122.1:8080/sony/"
camera_url = url+"camera"
avContent_url = url+"avContent"

def create_params_dict(method,params=[],id_=1,version="1.0"):
    params = collections.OrderedDict([
          ("method", method),
          ("params", params),
          ("id", id_),
          ("version", version)])
    return params

def api_call(url,params):
    return urllib2.urlopen(url,json.dumps(params))

def cast_params(param_list):
    #first object on param list ist method name, second the first param for api
    #call api_call for getMethodTypes
    #cast type for every argument on the param list
##    try:
    parameter_types = json.load(api_call(camera_url,list_of_method_types()))
    for i in parameter_types["results"]:
        if(i[0]==param_list[0]):
            if (i[1]!=None):
                for counter, to_type in enumerate(i[1]):
                    param_list[counter+1] = cast(param_list[counter+1],to_type)
##    except:
##        parameter_types = json.load(api_call(avContent_url,list_of_method_types()))
##        for i in parameter_types["results"]:
##            if(param_list != []):
##                if(i[0]==param_list[0]):
##                    if (i[1]!=None):
##                        for counter, to_tpye in enumerate(i[1]):
##                            param_list[counter+1] = cast(param_list[counter+1],to_type)
    return param_list

def cast(value, to_type):
    if (to_type=="int"):
        return int(value)
    
    if (to_type=="bool"):
        return bool(value)

    if (to_type=="string"):
        return str(value)

    if (to_type=="int*"):
        help_int = []
        for i in value:
            help_int.append(int(i))
        return help_int

    if (to_type=="string*"):
        help_string = []
        for i in value:
            help_string.append(str(i))
        return help_string

    if (to_type=="bool*"):
        help_bool = []
        for i in value:
            help_bool.append(bool(i))
        return help_bool
        
def list_of_method_types():
    params_for_api_call = collections.OrderedDict([
        ("method", "getMethodTypes"),
        ("params", ["1.0"]),
        ("id", 1),
        ("version", "1.0")])
    return params_for_api_call
                         
def command_line_call():
    if(len(sys.argv)==1):
        raw_params = ["getAvailableApiList"]
    else:
        raw_params =  sys.argv[1:]
    clean_params = cast_params(raw_params)
    if(len(clean_params)>1):
        params_for_api_call = create_params_dict(clean_params[0],clean_params[1:])
    else:
        params_for_api_call = create_params_dict(clean_params[0])
    print api_call(camera_url,params_for_api_call).read()
    
        

command_line_call()
