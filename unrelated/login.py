from appJar import gui

app = gui("Login")
def main():
    global app
    createLabel(app,"Login Window","Green","White",16)
    app.addLabelEntry("Username")
    app.addSecretLabelEntry("Password")
    app.addButtons(["Submit","Cancel","Reset"],press)
    app.addStatus()
    app.setStatus("New Status...")
    app.go()

def press(name):
    print(name,"pressed")
    global app
    if name=="Submit":
        user=app.getEntry("Username")
        pwd=app.getEntry("Password")
        verify_login(user,pwd)
    elif name=="Cancel":
        app.stop()
    elif name=="Reset":
        app.clearEntry("Username")
        app.clearEntry("Password")
        app.setFocus("Username")


def verify_login(Username,Password):
    global app
    if Username=="abcd" and Password == "abcd":
        app.infoBox("Success","Your Login details were accepted")
    else:
        app.errorBox("Error","Invalid Login Details")


def createLabel(app,name,bg,fg,size):
    app.addLabel(name,name)
    app.setBg(bg)
    app.setFg(fg)
    app.setFont(size)
    return

if __name__ == "__main__":
    main()
