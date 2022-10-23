import startbutton_functions
import tkinter as tk

#from asyncio.timeouts import timeout
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
options=startbutton_functions.get_portlist()

#print(re.match(r'COM\d',str(options[0])))
selected.set(' ')
drop_down=tk.OptionMenu(setup_window,selected,*options)
drop_down.pack()

#button to set
setup_label=tk.Label(setup_window,text="port is :")
setup_label.pack()
button = tk.Button(setup_window , text = "set port" , command = lambda: startbutton_functions.set_port_callback(selected,setup_window,setup_label)).pack() 

rec_label=tk.Label(setup_window,text='Sent:')
rec_label.pack()
start_button=tk.Button(setup_window,text='Start',command= lambda: startbutton_functions.start_button_callback(selected,rec_label)).pack()

setup_window.mainloop()