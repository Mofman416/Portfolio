#Michael Freeman
from tkinter import *


class Calculator(Frame):
    """Initialize the Calculator program."""

    def __init__(self, master):
        """This sets up the calculator"""
        super(Calculator, self).__init__(master)
        self.grid()
        self.window()

    def window(self):
        """Updates the text as the user clicks buttons"""
        """This sets up the text field."""
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)
        formula = "I work!"
        if self.nums1.get():
            pass
            #formula += nums1

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, formula)


root = Tk()
root.title("Calculator")
app = Calculator(root)

root.mainloop()
