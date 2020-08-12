from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(app, text = "I do nothing!")
        self.bttn1.grid()

        self.bttn2 = Button(app)
        self.bttn2.grid()
        self.bttn2.configure(text = "Don't click me.")
        self.bttn2.configure(bg = "yellow")
        self.bttn2.configure(fg="red")

        self.bttn3 = Button(app)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"
        self.bttn3["bg"] = "Blue"
        self.bttn3["fg"] = "Green"



root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)

root.mainloop()