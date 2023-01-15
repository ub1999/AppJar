# AppJar
### Dependencies:
  - appJar(Not anymore, I use tkinter now which is in standed python library)
  - pyserial
  - look at the [serialtesting_arduino_script](https://github.com/ub1999/AppJar/tree/main/serialtesting_arduino_script) repo for arduino script
    - right now this script is just sending numbers in 5 sec intervals. 
  - the serial_test.py is the python script for reading arduino's serial output 
  
### How to use the startbutton.py GUI
  - Run the startbutton.py for the actual serial gui
    - First select the port from drop down menu, 
    - then click set port
    - you can only start using the gui now 
    - Space above start/stop button shows what message was revieced by arduiono. The default value there says "Sent:" 
    - click start button, stop button, or enter text and click "Send Message" button
    - if you press "listen" a new window open, that is listening to the serial port. and will display the information coming into the port. 
      - this information if decoded using 'utf' format and then displayed on this new window
    - if you want to look at all the messages recieved during the current sesion, open the message_logs.txt to view all the messages that came into the biffer sequentially. 
