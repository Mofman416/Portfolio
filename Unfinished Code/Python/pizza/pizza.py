# Michael Freeman
from tkinter import *
from tkinter.ttk import Combobox


class Pizza(Frame):
    """Initialize the Pizza program"""

    def __init__(self, master):
        """This sets up the Pizza program"""
        super(Pizza, self).__init__(master)
        self.grid()  # This is absolutely vital for future GUI projects!
        self.name = ""
        self.size = StringVar()
        self.size.set(value="small")
        self.create_widgets()


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

        self.size_sml = Radiobutton(self, variable=self.size, value="small", text="Small")
        self.size_sml.grid(row=1, column=1)

        self.size_med = Radiobutton(self, variable=self.size, value="medium", text="Medium")
        self.size_med.grid(row=1, column=2)

        self.size_lrg = Radiobutton(self, variable=self.size, value="large", text="Large")
        self.size_lrg.grid(row=1, column=3)

        # Adds ComboBox
        self.crust_label = Label(self, text="Crust:")
        self.crust_label.grid(row=2, column=0)

        self.crust_selection = Combobox(self,
                                        values=[
                                            "Thin",
                                            "Thick",
                                            "Deep dish"
                                        ])
        self.crust_selection.grid(row=2, column=1, columnspan=3)

        # Adds Listbox
        self.toppings_label = Label(self, text="Toppings:")
        self.toppings_label.grid(row=3, column=0)

        self.toppings_selection = Listbox(self)
        self.toppings_selection.grid(row=3, column=1)
        self.toppings_selection.insert(1, "Pepperoni")
        self.toppings_selection.insert(2, "Sausage")
        self.toppings_selection.insert(3, "Green Peppers")
        self.toppings_selection.insert(4, "Olives")
        self.toppings_selection.insert(5, "Chicken")


root = Tk()
root.title("Order Pizza")
root.resizable(width=False, height=False)
app = Pizza(root)

root.mainloop()
