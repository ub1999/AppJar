
#imports
from asyncore import read
from cgitb import text
import serial
import serial.tools.list_ports as port_list
import time
import os
import tkinter as tk
from turtle import position, title, window_height, window_width
import string
import re
from sys import platform



def get_portlist():
    portlist=[]
    for p in port_list.comports():
        #print(p)
        portlist.append({p.name,p.description})
    #print("Current ports on device:")
    return(portlist)    

def set_port_callback(dropdownitem:tk.StringVar,window: tk.Tk,label_item:tk.Label): 
    label_item.config(text='Port is now: '+dropdownitem.get())

def start_button_callback(DropDownItem:tk.StringVar, test_label:tk.Label,message='start'):
    port_no=''
    
    #write a code for linux laptops:
    if platform == "linux" or platform == "linux2":
    # linux
       port_no='/dev/'+re.search(r"({')(\w+)('})",DropDownItem.get()).group(2)
    elif platform == "darwin":
        # OS X
        print('yeah sorry I have no clue')
    elif platform == "win32":
    # Windows...
        port_no=re.search(r'COM\d',DropDownItem.get()).group()
        
    print(port_no)
    
    with serial.Serial(port_no,115200,timeout=2) as ser:
        print('connected to port',ser.portstr)
        print("setup complete")
        #check if something is in the serial input buffer
        if ser.in_waiting==0:
            print('Sending:'+message)
            recieved_packet=ser.read_until()
            message=message+'\n'
            ser.write(message.encode('utf-8'))
            #print('sending a packet',recieved_packet)
        recieved_packet=ser.read_until()
        test_label.config(text=recieved_packet.decode('utf')) 
        print(recieved_packet.decode('utf'))


        