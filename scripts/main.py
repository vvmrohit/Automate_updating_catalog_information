#!/usr/bin/env python3

import reports
import emails
import os
from datetime import datetime


def main():
    description_file_path = ''
    os.chdir(description_file_path)
    description = []
    for infile in os.listdir(description_file_path):
        with open(infile, 'r') as file:
            data = file.split('\n')
            dict = {}
            dict["name"] = data[0]
            dict["weight"] = data[1]
            description.append(dict)
        
    #This is the part where we need to generate report
    pdf_body = ""
    current_datetime = datetime.now()
    formated_date = current_datetime.strftime("%B %d, %Y")
    title = "Processed Update on {}".format(formated_date)
    reports.generate("processed.pdf",title,pdf_body)


    #This is where we will send mail.
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    sender = "automation@example.com"
    reciver = "username@example.com"
    Subject = "Upload Completed - Online Fruit Store"
    message = emails.generate(sender,reciver,Subject,body,"")
    




if __name__=="__main__":
    main()