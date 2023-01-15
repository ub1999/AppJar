
#imports
import asyncio
from asyncore import read
from cgitb import text
from collections import deque
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
    f=open('message_logs.txt','w')
    f.close()
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
    #queue containing listened values
    q=deque()
    # start a thread that listening to messages coming into the port. I used threads so that the rest of the GUI can be 
    # interacted with during the while loop. 
    listen_thread=threading.Thread(target=listen_coro,args=(q,),daemon=True)
    listen_thread.start()
    print("started: listen thread")

    #the following thread just updates the GUI with the newest info 
    update_thread=threading.Thread(target=update_listen_window,args=(listen_label,q,),daemon=True)
    update_thread.start()
    print("started: Screen update thread ")
   
    listen_window.mainloop()

    

def update_listen_window(test_label:tk.Label,q):
    #will update the listen window with the last 3 entries in listen window
    while True:
       #if something new was added to queue, display it
       if len(q)>0:
           test_label.config(text=test_label.cget('text')+'\n'+ str(datetime.now()) + ' : ' + q.popleft())
       else:
           time.sleep(1) #1 sec sleep if nothing in queue


def listen_coro(q):
    #listen to the port and save the incoming data and add it to q then save it in message_logs.txt
    while True: 
        if ser1.inWaiting():
            recieved_packet=ser1.readline()
            recieved_packet=recieved_packet[0:len(recieved_packet)-2].decode("utf")
            print(recieved_packet)
            q.append(recieved_packet)
            #test_label.config(text=str(recieved_packet))
            save_data_coro(str(recieved_packet))
        else :
            time.sleep(1) # 1 sec sleep if nothing in serial buffer. 

def save_data_coro(recieved_packet):
    #saves the recieved packet string into a txt file
    f=open('message_logs.txt','a')
    # time object + recieved data into logfile
    f.write(str(datetime.now().time())+':'+recieved_packet+'\n')
    f.close()


ser1.close()

        