#!/opt/homebrew/bin/python3

##/usr/bin/env python3

#importing libraries
import os
import requests
import json

#setting description location and switching to it
description_file_path = ''
os.chdir(description_file_path)

description = []

for infile in os.listdir(description_file_path):
    filename ,ext = os.path.splitext(infile)
    with open(infile, 'r') as file:
        data = file.split('\n')
        dict = {}
        dict["name"] = data[0]
        dict["weight"] = int(data[1][:-4])
        dict["description"] = data[2]
        dict ["image_name"] = filename +"jpeg"
        description.append(dict)


headers = {"Content-Type": "application/json; charset=utf-8"}
url = "http://localhost/fruits/"
for dict in description:
    json_body = json.dumps(dict)
    requests.post(url,headers=headers, json=json_body)




        
         