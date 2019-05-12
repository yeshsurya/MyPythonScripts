# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:32:20 2019

@author: 212744433
"""

import paramiko
import sys

nbytes = 4096
hostname = '3.204.36.157'
port = 22
username = 'sdc' 
password = 'adw2.0'
command = 'swic'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print('exit status: ', session.recv_exit_status())
print(stdout_data)
print('Standard Error Output is : ')
print(stderr_data)

session.close()
client.close()