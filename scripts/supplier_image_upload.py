#!/opt/homebrew/bin/python3

##/usr/bin/env python3

#importing libraries

import requests
import glob
import os

#setting image path and switching to it
image_path = "/Users/rohitpandey/Documents/github_cloned_repo/Automate_updating_catalog_information/supplier-data/images"
os.chdir(image_path)


#Main code to upload all jpeg file to server using requests module
url = "http://localhost/upload/"

for infile in glob.glob("*/jpeg"):
    with open(infile, 'rb') as im:
        r = requests.post(url, files={'file': im})

