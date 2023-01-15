
#imports
import asyncio
from asyncore import read
from cgitb import text
from lib2to3.pgen2.token import STRING
from pickle import TRUE
from stringprep import in_table_a1
import serial
import serial.tools.list_ports as port_list
import time
import os
import tkinter as tk
from turtle import position, title, window_height, window_width
import string
import re
import asyncio
import threading
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
#create listen window
def create_listen_window():
    listen_window=tk.Tk()
    listen_window.title("Incoming Data")
    listen_window.geometry("300x300")
    listen_label=tk.Label(listen_window,text="incoming:")
    listen_label.pack()
    listen_button = tk.Button(listen_window,text="Listen", command=lambda: startbutton_functions.listen_button_callback(listen_label))
    listen_button.pack()

def listen_button_callback():
    listen_window=tk.Tk()
    listen_window.title("Incoming Data")
    listen_window.geometry("300x300")
    listen_label=tk.Label(listen_window,text="incoming:")
    listen_label.pack()
    print("creating listen thread")
    x=threading.Thread(target=listen_coro,args=(listen_label,),daemon=True)
    x.start()
    print("Thread Started")

    #create a new display function because I cant display the data rn 
    with open('message_logs.txt','r') as f:
    # time object + recieved data into logfile
        txt=''
        for line in f.readlines()[-1:]:
            txt=[txt,line]
        listen_label.config(text=str(txt))
    



def listen_coro(test_label:tk.Label):
    #listen to the aforementioned port, asynchornously
    while True: 
        if ser1.inWaiting():
            recieved_packet=ser1.readline()
            recieved_packet=float(recieved_packet[0:len(recieved_packet)-2].decode("utf"))
            print(recieved_packet)
            #test_label.config(text=str(recieved_packet))
            save_data_coro(str(recieved_packet))
        else :
            time.sleep(5)

def save_data_coro(recieved_packet):
    #do something
    f=open('message_logs.txt','a')
    # time object + recieved data into logfile
    f.write(str(datetime.now().time())+':'+recieved_packet+'\n')
    f.close()


ser1.close()

        