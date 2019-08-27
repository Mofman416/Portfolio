# Michael Freeman
from tkinter import *

class Pizza(Frame):
    """Initialize the Pizza program"""

    def __init__(self, master):
        """This sets up the Pizza program"""
        super(Pizza, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """This creates the input types"""
        self.name = Label(self, text="Name: ", )
        self.name.grid(row=0, column=0)

        self.entername = Text(self)
        self.entername.grid(row=0, column=1)


root = Tk()
root.title("Order Pizza")
root.resizable(width=False, height=False)
app = Pizza(root)

root.mainloop()
