#!/usr/bin/env python3

import psutil
import socket
import time
import health_emails

def main():
    cpu_threshold = 80
    disk_space = 20
    memory = 500
    hostname = "127.0.0.1"
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage("/")
    available_memory = psutil.virtual_memory().available / (1024 * 1024)
    resolved_ip = socket.gethostbyname("localhost")
    sender = "automation@example.com"
    reciver = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    if cpu_usage > cpu_threshold:
        subject = "Error - CPU usage is over 80%"
        cpu_message = health_emails.generate(sender,reciver,subject,body)
        health_emails.send(cpu_message)
    if disk_usage < disk_space:
        subject = "Error - Available disk space is less than 20%"
        disk_message = health_emails.generate(sender,reciver,subject,body)
        health_emails.send(disk_message)
    if available_memory < memory:
        subject = "Error - Available memory is less than 500MB"
        memory_message = health_emails.generate(sender,reciver,subject,body)
        health_emails.send(memory_message)
    if resolved_ip!= hostname:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        ip_message = health_emails.generate(sender,reciver,subject,body)
        health_emails.send(ip_message)



if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)