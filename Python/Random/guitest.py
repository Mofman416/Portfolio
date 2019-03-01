#Simple GUI
# Demonstrates creating a window

from tkinter import *

#create the root window
root = Tk()

#modify the window
root.title("Simple GUI")
root.geometry("200x100")
root.configure(bg = "green")

app = Frame(root)
app.grid()

label = Label(app, text = "this is a fancy label")
lbl = Label(app, text = "I'm a label!")
lb2 = Label(app, text = "Another one!")
lb2.grid()
label.grid()
lbl.grid()

lbl.config(font = ("Courier", 44))
lbl.config(foreground = "orange")
lbl.config(bg = "blue")
#kick off the window's event-loop
root.mainloop()