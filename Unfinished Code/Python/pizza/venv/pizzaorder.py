# Michael Freeman

from tkinter import *

class Pizza(Frame):
    """Initialize the Pizza Order Program"""

    def __init__(self, master):
        """This sets up the pizza ordering program"""
        super(Pizza, self).__init__(master)

root = Tk()
root.title("Pizza Root")
root.resizable(width=False, height=False)
app = Pizza(root)

root.mainloop()
