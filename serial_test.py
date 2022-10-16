import serial
import time

#make sure you choose the correct COM# port for your own computer
with serial.Serial('COM3',9600) as ser:
    #ser.open()
    print("connected to port",ser.portstr,"\n")
    print(ser.readlines().decode("utf"))
    while(True):
        if ser.in_waiting:
            packet=ser.readlines()
            print("read from arduino:")
            print(packet.decode('utf')) #because arduino sends info in utf to serial, we want it to be understandable so wee decode

    