# import the library
from appJar import gui
#press function(event) recieves the name of the button as a parameter upon click
count = 0
def press(name):

    # try:
    #     press.count+=1
    # except AttributeError:
    #     press.count=0
    app.setBg(switch_color())
    global count
    count+=1
    app.setLabel("lb1","Pressed "+str(10-count)+" attempts left")
    if 10-count==0:
        app.stop()
    print(name,"button pressed")
    return

def switch_color():
    arr=["green","yellow","blue","red","white","black"]
    global count
    return arr[count%5]

# create a GUI variable called app
app = gui("Hello")
#create widgets(Label)
app.addLabel("lb1","Hello World")
app.addLabel("lb2","is it me you're looking for?")
#set window backgrounds and characteristics
app.setBg("Black")
app.setLabelBg("lb1","yellow")
app.setLabelBg("lb2","green")
app.setFont(20)
app.setSize("400x200")
app.setResizable("True")

#add button
app.addButton("Switch Colors",press)

app.go()
