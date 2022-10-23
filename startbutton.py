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

#from asyncio.timeouts import timeout



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
    #this line: uses a regex.search to look for a match for COM# from the chosen dropdown value, group() returns the matched string
    port_no=re.search(r'COM\d',DropDownItem.get()).group()
    with serial.Serial(port_no,115200,timeout=2) as ser:
        print('connected to port',ser.portstr)
        print("setup complete")
        #check if something is in the serial input buffer
        if ser.in_waiting==0:
            recieved_packet=ser.read_until()
            message=message+'\n'
            ser.write(message.encode('utf-8'))
            #print('sending a packet',recieved_packet)
        recieved_packet=ser.read_until()
        test_label.config(text=recieved_packet.decode('utf')) 
        print(recieved_packet.decode('utf'))


        
    

#setup window settings
setup_window= tk.Tk()
setup_window.title('Setup')

#set spaceteam logo as icon
logo=tk.PhotoImage(file='logo.png')
setup_window.iconphoto(False,logo)

#window dimensions
screendim=(int(setup_window.winfo_screenwidth()),int(setup_window.winfo_screenheight()))
pos=(screendim[0]/2,screendim[1]/2)
window_width=300
window_height=200
center_x=int(pos[0]-window_width/2)
center_y=int(pos[1]-window_height/2)
setup_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#create a dropdown button that lets you select a port 
info=tk.Label(setup_window,text='Please choose a serial port:')
info.pack()
selected=tk.StringVar()
options=get_portlist()
#print(re.match(r'COM\d',str(options[0])))
selected.set(' ')
drop_down=tk.OptionMenu(setup_window,selected,*options)
drop_down.pack()
#button to set
setup_label=tk.Label(setup_window,text="port is :")
setup_label.pack()
button = tk.Button(setup_window , text = "set port" , command = lambda: set_port_callback(selected,setup_window,setup_label)).pack() 

rec_label=tk.Label(setup_window,text='Sent:')
rec_label.pack()
start_button=tk.Button(setup_window,text='Start',command= lambda: start_button_callback(selected,rec_label)).pack()

setup_window.mainloop()