from asyncore import read
import serial
import serial.tools.list_ports as port_list
import time
import os
#from asyncio import timeout

def select_port():
    portlist=[]
    for p in port_list.comports():
        #print(p)
        portlist.append({p.name,p.description})
    
    print("Current ports on device:")
    print(portlist)    
    port_no = "COM" + input("Which port no. is the arduino connected to ?: COM")
    return port_no
#make sure you choose the correct COM# port for your own computer 

with serial.Serial(select_port(),115200) as ser:
        #ser.open()
        ser.timeout=1
        #doesnt read the first sent packet unless i have this in there
        packet=ser.read_until()
        print("You have connected to port",ser.portstr,"\n")
        ser.write("setup complete".encode('utf-8'))
        print("setup complete")
        while(True):
            if ser.in_waiting==0: #in_waiting Get the number of bytes in the input buffer
                print("port available")
                message=input("input data:")+"\n"
                ser.write(message.encode('utf-8'))#encodes input data into 8bit data
                print("packet sent")
                packet=ser.read_until()
                #ser.flush()
                #ser.reset_input_buffer()
                print(packet.decode('utf')) #because arduino sends info in utf to serial, we want it to be understandable so wee decode
            else:
                packet=ser.read_until()#removes the /r/c parity data that was sent... i think 