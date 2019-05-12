# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:49:04 2019

@author: yeshsurya / SWCI GUI tool
"""
from tkinter import *
import tkinter.ttk as ttk
import paramiko
import sys
username = 'sdc' 
password = 'adw2.0'
port = 22
nbytes = 4096
lines={}
result = ''
def load_machineIPs():
    try : 
        lines = [line.rstrip('\n') for line in open('machineips')]
        return lines
    except FileNotFoundError : 
        pass
def execute_swic_command(hostname):
    stdout_data = []
    stderr_data = []
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    session = client.open_channel(kind='session')
    session.exec_command("swic")
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break
    print('exit status: ', session.recv_exit_status())
	result = stdout_data
    print(stdout_data)
    print('Standard Error Output is : ')
    print(stderr_data)
    session.close()
    client.close()
def show_entry_fields():
   command_string = cb.get()
   machine_ip = e1.get()
   print("Machine IP: %s\n Command String %s" % (machine_ip,command_string))
   if command_string == "SWIC":
       print("Executing SWIC command")
       print(machine_ip)
       execute_swic_command("3.204.36.191")
   e1.delete(0,END)
   

master = Tk()
lines=load_machineIPs()
master.geometry("350x330")
foo=Text(master,height=10, width=20)
master.winfo_toplevel().title("SSH2UNIX")
Label(master, text="Machine IP").grid(row=0)
Label(master, text="RESULT : ").grid(row=2)
print("Printinglines")
print(lines)
e1 = ttk.Combobox(master,values=tuple(lines),state="readonly")
#"3.204.36.157", "3.204.36.155", "3.204.36.236", "3.204.36.194", "3.204.36.199"
e1.insert(10,"Miller")
e1.grid(row=0, column=1)
cb = ttk.Combobox(master, values=("SWIC", "ls", "alscoa", "merge", "newview"), state="readonly")
cb.grid(row=2, column=1)
foo.grid(row=4,column=1)
Button(master, text='Close', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Fetch', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)

mainloop( )
