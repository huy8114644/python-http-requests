#!/usr/bin/python
import json
import re

#write file
def write_file(data) :
    f1 = open ( 'food.txt', 'a')
    json.dumps(data, f1)

#read file
def read_file () :
    f2 = open ( 'food.txt', 'r')
    return f2.read()

#add json
def add_json (json_string, index) :
    # convert it to a python dictionary
    json_dict = json.loads(json_string)
    json_dict = [k.replace('u\'','') for k in json_dict]
    # append your data as {key:value}
    print (json_dict)
    #json_dict[index].append({'name':'test3'})
    # convert it back to string
    #json_string = json.dumps(json_dict)
    #print (json_string)

    