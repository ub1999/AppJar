
#imports
from asyncore import read
from cgitb import text
from stringprep import in_table_a1
import serial
import serial.tools.list_ports as port_list
import time
import os
import tkinter as tk
from turtle import position, title, window_height, window_width
import string
import re
from sys import platform
from datetime import datetime

ser1=serial.Serial()
recieved_packet=''

def get_portlist():
    portlist=[]
    for p in port_list.comports():
        #print(p)
        portlist.append({p.name,p.description})
    #print("Current ports on device:")
    return(portlist)    

def set_port_callback(DropDownItem:tk.StringVar,window: tk.Tk,label_item:tk.Label): 
    ser1.baudrate=115200
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
    ser1.port=port_no
    ser1.timeout=0.9
    ser1.close()
    label_item.config(text='Port is now: '+port_no)
    print('connected to port',ser1.portstr)
    print("setup complete")
    ser1.open()
    #save all exchanged messages into this file 
    #f=open('message_logs.txt','w')
    #somehow everything fallsapart without this i dont understand why
    recieved_packet=ser1.read_until().decode('utf')

def start_button_callback(DropDownItem:tk.StringVar, test_label:tk.Label,message='start'):    
    message=message+'\n'
    ser1.write(message.encode('utf-8'))
    print('Sending:'+message)
    recieved_packet=''
    #wait for out buffer to be empty
    while ser1.out_waiting:
        continue
    #print(r'write buffer empty')
    while 1: 
    #print(r'read buffer not empty',ser1.in_waiting)
        if ser1.in_waiting:   
            while ser1.in_waiting:
                #print('in read buffer a packet')
                recieved_packet=recieved_packet + ser1.read_until().decode('utf')
                recieved_packet=str(re.sub(r'[\n]',"",recieved_packet,count=1))
            recieved_packet=str(re.sub(r'rec:',"",recieved_packet))
            test_label.config(text="rec:"+recieved_packet)

            #first overwrite pre-exiting content with rec:
            #f.write('rec:\n');f.close()
            #then only append whatever messages were recieved from arduino over this session 
            f=open('message_logs.txt','a')
            # time object + recieved data into logfile
            f.write(str(datetime.now().time())+':'+recieved_packet+'\n')
            f.close()
            break
        else:
            pass

def listen_button_callback(test_label:tk.Label):
    #recieved_packet=''
    while 1:
        try:
            recieved_packet=ser1.readline()
            recieved_packet=float(recieved_packet[0:len(recieved_packet)-2].decode("utf"))
            print(recieved_packet)
            test_label.config(text="rec:"+recieved_packet)
            f=open('message_logs.txt','a')
            # time object + recieved data into logfile
            f.write(str(datetime.now().time())+':'+recieved_packet+'\n')
            f.close()
        except:
            print ("Keyboard Interrupt")
            break
ser1.close()

        