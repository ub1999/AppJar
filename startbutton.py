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
window_height=300
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
rec_label=tk.Label(setup_window,bg='white',text='Sent:')
rec_label.pack()
#start button
start_button=tk.Button(setup_window,text='Start',bg='green',command= lambda: startbutton_functions.start_button_callback(selected,rec_label)).place(relx=0.25,rely=0.40)
#stop button 
stop_button=tk.Button(setup_window,text='Stop',bg='red',command= lambda: startbutton_functions.start_button_callback(selected,rec_label,message="stop")).place(relx=0.62,rely=0.4)

#custon text button 
tk.Label(setup_window,text='\n').pack()
textbox=tk.Entry(setup_window,text='Enter command here')
textbox.pack()
message_button=tk.Button(setup_window,text='Send Message',command= lambda: startbutton_functions.start_button_callback(selected,rec_label,message=textbox.get())).pack()



# create a button
listen_button = tk.Button(setup_window,text="Listen", command=lambda: startbutton_functions.listen_button_callback())
listen_button.pack()

#listen_button=tk.Button(setup_window,text='Listen',command= lambda: startbutton_functions.listen_button_callback(rec_label)).pack()
setup_window.mainloop()