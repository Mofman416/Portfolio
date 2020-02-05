# Michael Freeman
from tkinter import *

class Pizza(Frame):
    """Initialize the Pizza program"""

    def __init__(self, master):
        """This sets up the Pizza program"""
        super(Pizza, self).__init__(master)
        self.grid()  # This is absolutely vital for future GUI projects!
        self.create_widgets()
        self.name = ""
        self.size = StringVar
        self.size.set(self, value="Small")

    def create_widgets(self):
        """This creates the input types"""
        # Adds text field for username entry
        self.name_label = Label(self, text="Name: ")
        self.name_label.grid(row=0, column=0)

        self.entername = Text(self, width=35, height=1)
        self.entername.grid(row=0, column=1, columnspan=3)

        # Adds Radiobuttons for users to interact with
        self.size_label = Label(self, text="Size:")
        self.size_label.grid(row=1, column=0)

        self.size_sml = Radiobutton(self, variable=self.size, value="Small", text="Small")
        self.size_sml.grid(row=1, column=1)

        self.size_med = Radiobutton(self, variable=self.size, value="Medium", text="Medium")
        self.size_med.grid(row=1, column=2)

        self.size_lrg = Radiobutton(self, variable=self.size, value="Large", text="Large")
        self.size_lrg.grid(row=1, column=3)


root = Tk()
root.title("Order Pizza")
root.resizable(width=False, height=False)
app = Pizza(root)

root.mainloop()
