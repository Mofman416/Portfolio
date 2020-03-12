# Michael Freeman
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mb


class Pizza(Frame):
    """Initialize the Pizza program"""

    def __init__(self, master):
        """This sets up the Pizza program"""
        super(Pizza, self).__init__(master)
        self.grid()  # This is absolutely vital for future GUI projects!
        self.name = ""
        self.size = StringVar()
        self.size.set(value="Small")
        self.create = StringVar()
        self.soda = IntVar()
        self.bread = IntVar()
        self.salad = IntVar()
        self.create.set(value="None")
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

        self.size_sml = Radiobutton(self, variable=self.size, value="Small", text="Small")
        self.size_sml.grid(row=1, column=1)

        self.size_med = Radiobutton(self, variable=self.size, value="Medium", text="Medium")
        self.size_med.grid(row=1, column=2)

        self.size_lrg = Radiobutton(self, variable=self.size, value="Large", text="Large")
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

        self.toppings_selection = Listbox(self, selectmode="multiple")
        self.toppings_selection.grid(row=3, column=1, columnspan=3)
        self.toppings_selection.insert(1, "Pepperoni")
        self.toppings_selection.insert(2, "Sausage")
        self.toppings_selection.insert(3, "Green Peppers")
        self.toppings_selection.insert(4, "Olives")
        self.toppings_selection.insert(5, "Chicken")

        # Adds Checkboxes
        self.sides_label = Label(self, text="Sides:")
        self.sides_label.grid(row=4, column=0)

        self.sides_soda = Checkbutton(self, text="Soda", variable=self.soda)
        self.sides_soda.grid(row=4, column=1)

        self.sides_bread = Checkbutton(self, text="Bread Sticks", variable=self.bread)
        self.sides_bread.grid(row=4, column=2)

        self.sides_salad = Checkbutton(self, text="Salad", variable=self.salad)
        self.sides_salad.grid(row=4, column=3)

        # Adds order comments, which is a larger text field
        self.comment_label = Label(self, text="Order Comments")
        self.comment_label.grid(row=5, column=0)

        self.comment = Text(self, width=35, height=5)
        self.comment.grid(row=5, column=1, columnspan=3)

        # Adds a confirmation or erasure button
        self.confirm = Button(self, text="Confirm", width=7, command=self.confirmOrder)
        self.confirm.grid(row=6, column=1)

        self.deny = Button(self, text="Clear", width=7)
        self.deny.grid(row=6, column=2)

    def confirmOrder(self):
        side = []
        try:
            toppings = self.toppings_selection.get(self.toppings_selection.curselection())
        except TclError:
            toppings = "Error! Please select only one topping."
        name = self.entername.get("1.0", "end-1c")
        size = self.size.get()
        crust = self.crust_selection.get()
        if self.soda.get() == 1:
            side.insert(0, "Soda")
        if self.bread.get() == 1:
            side.insert(1, "Bread")
        if self.salad.get() == 1:
            side.insert(2, "Salad")
        side_display = side
        #side = self.sides.get()
        comment = self.comment.get("1.0", "end-1c")
        mb.showinfo("Confirm", "Name: " + name + "\n" "Size: " + size + "\n" + "Crust Type: " + crust + "\n" +
                    "Toppings: " + toppings + "\n" + "Sides: " + side +
                    "\n" + "Order Comments: " + comment)

    def clearOrder(self):
        self.entername = ""
        self.comment = ""


root = Tk()
root.title("Order Pizza")
root.resizable(width=False, height=False)
app = Pizza(root)

root.mainloop()
