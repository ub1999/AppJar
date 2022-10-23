import string
import tkinter as tk
from turtle import position, window_height, window_width
from asyncore import read



root = tk.Tk()
root.title('tkinter window demo')
# this command fetches the window title : title=root.title()

""" 
widgets look like this widget = WidgetName(container, **options)
place a label widget on the root window 
"""

message = tk.Label(root, text="Hello, World!")
#positions the widget on the root window
message.pack()

# size and position of a window :widthxheight±x±y
screendim=(int(root.winfo_screenwidth()),int(root.winfo_screenheight()))
pos=(screendim[0]/2,screendim[1]/2)
window_width=300
window_height=200
center_x=int(pos[0]-window_width/2)
center_y=int(pos[1]-window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#decides whether window is resizable or not window.resizable(width,height)
root.resizable(False,False)

""" 
to limit resizability of a window use the following setting:
window.minsize(min_width, min_height)
window.maxsize(min_height, max_height) 
"""

""" 
transparency settings
window.attributes('-alpha',0.5)
"""


'''
Summary

    Use the title() method to change the title of the window.
    Use the geometry() method to change the size and location of the window.
    Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
    Use the window.attributes('-alpha',0.5) to set the transparency for the window.
    Use the window.attributes('-topmost', 1) to make the window always on top.
    Use lift() and lower() methods to move the window up and down of the window stacking order.
    Use the iconbitmap() method to change the default icon of the window.
'''

start_button=tk.Button(
    root,
    text='Start',
    width=25,
    height=5,
    bg='red',
    fg='white',
    #command=serial_test.send_message("Start \n") write a function that only sends a start message 
)
start_button.pack()
# serial_message=tk.Entry(fg='black')
# serial_message.pack()

# keep the window displaying
root.mainloop()