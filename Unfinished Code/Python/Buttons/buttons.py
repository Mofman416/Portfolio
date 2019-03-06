from tkinter import *
from tkinter import font

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")
root.configure(bg="Red")


app = Frame(root)
app.grid()
app.configure(bg = "green")


bttn1 = Button(app, text="I do nothing!")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="Don't click me.")
bttn2.configure(bg = "yellow")
bttn2.configure(fg = "red")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"

root.mainloop()