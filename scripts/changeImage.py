#!/opt/homebrew/bin/python3

##/usr/bin/env python3
#importing libraries
from PIL import Image
import os

#Specifying image path and switching to it
image_path = "/Users/rohitpandey/Documents/github_cloned_repo/Automate_updating_catalog_information/supplier-data/images"
os.chdir(image_path)


#Main code where we are resizing the path and saving it as 
for filename in os.listdir(image_path):
    file, ext = os.path.splitext(filename)
    with Image.open(filename) as im:
        rgb_im = im.convert('RGB')
        out = rgb_im.resize((600, 400))
        out.save(file + ".jpeg")

