#Michael Freeman
from tkinter import *


class Calculator(Frame):
    """Initialize the Calculator program."""

    def __init__(self, master):
        """This sets up the calculator"""
        super(Calculator, self).__init__(master)
        self.display = ""
        self.position1 = ""
        self.position2 = ""
        self.operator = ""
        self.grid()
        self.create_widgets()


    def create_widgets(self):

        self.results_txt = Text(self, width=35, height=5, wrap=WORD)
        self.results_txt.grid(row=0, column=0, columnspan=4)

        self.bttn1 = Button(self, command = self.btt1, width = 8, height = 2)
        self.bttn1["text"] = "1"
        self.bttn1.grid(row = 1, column = 0)

        self.bttn2 = Button(self, command = self.btt2, width = 8, height = 2)
        self.bttn2["text"] = "2"
        self.bttn2.grid(row = 1, column = 1)

        self.bttn3 = Button(self, command = self.btt3, width = 8, height = 2)
        self.bttn3["text"] = "3"
        self.bttn3.grid(row = 1, column = 2)

        self.bttn4 = Button(self, command = self.btt4, width = 8, height = 2)
        self.bttn4["text"] = "4"
        self.bttn4.grid(row = 2, column = 0)

        self.bttn5 = Button(self, command = self.btt5, width = 8, height = 2)
        self.bttn5["text"] = "5"
        self.bttn5.grid(row = 2, column = 1)

        self.bttn6 = Button(self, command = self.btt6, width = 8, height = 2)
        self.bttn6["text"] = "6"
        self.bttn6.grid(row = 2, column = 2)

        self.bttn7 = Button(self, command = self.btt7, width = 8, height = 2)
        self.bttn7["text"] = "7"
        self.bttn7.grid(row = 3, column = 0)

        self.bttn8 = Button(self, command = self.btt8, width = 8, height = 2)
        self.bttn8["text"] = "8"
        self.bttn8.grid(row = 3, column = 1)

        self.bttn9 = Button(self, command = self.btt9, width = 8, height = 2)
        self.bttn9["text"] = "9"
        self.bttn9.grid(row = 3, column =2)

        self.bttn0 = Button(self, command = self.btt0, width = 8, height = 2)
        self.bttn0["text"] = "0"
        self.bttn0.grid(row = 4, column = 0)

        self.bttne = Button(self, command = self.equ, width = 8, height = 2)
        self.bttne["text"] = "="
        self.bttne.grid(row = 4, column = 1)

        self.bttnc = Button(self, command = self.clear, width = 8, height = 2)
        self.bttnc["text"] = "C"
        self.bttnc.grid(row = 4, column = 2)

        self.bttnp = Button(self, command = self.add, width = 8, height = 2)
        self.bttnp["text"] = "+"
        self.bttnp.grid(row = 1, column = 3)

        self.bttnmi = Button(self, command = self.minus, width = 8, height = 2)
        self.bttnmi["text"] = "-"
        self.bttnmi.grid(row = 2, column = 3)

        self.bttnmu = Button(self, command = self.multiply, width = 8, height = 2)
        self.bttnmu["text"] = "X"
        self.bttnmu.grid(row = 3, column = 3)

        self.bttnd = Button(self, command = self.divide, width = 8, height = 2)
        self.bttnd["text"] = "/"
        self.bttnd.grid(row = 4, column = 3)

    def btt1(self):
        self.display +="1"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt2(self):
        self.display +="2"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt3(self):
        self.display +="3"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt4(self):
        self.display +="4"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt5(self):
        self.display +="5"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt6(self):
        self.display +="6"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt7(self):
        self.display +="7"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt8(self):
        self.display +="8"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt9(self):
        self.display +="9"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def btt0(self):
        self.display += "0"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)

    def add(self):
        self.position1 = self.display
        self.operator = "+"
        self.results_txt.delete(0.0, END)
        self.display = ""

    def minus(self):
        self.position1 = self.display
        self.operator = "-"
        self.results_txt.delete(0.0, END)
        self.display = ""

    def multiply(self):
        self.position1 = self.display
        self.operator = "X"
        self.results_txt.delete(0.0, END)
        self.display = ""

    def divide(self):
        self.position1 = self.display
        self.operator = "/"
        self.results_txt.delete(0.0, END)
        self.display = ""

    def clear(self):
        self.position1 = ""
        self.operator = ""
        self.results_txt.delete(0.0, END)
        self.position2 = ""
        self.display = ""

    def equ(self):
        self.position2 = self.display
        if self.operator == "+":
            self.display = int(self.position1) + int(self.position2)

        elif self.operator == "-":
            self.display = int(self.position1) - int(self.position2)

        elif self.operator == "X":
            self.display = int(self.position1) * int(self.position2)

        elif self.operator == "/":
            try:
                self.display = float(self.position1) / float(self.position2)
            except:
                self.display = "Can't divide by 0."

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.display)
        self.display = ""


root = Tk()
root.title("Calculator")
root.resizable(width = False, height = False)
app = Calculator(root)

root.mainloop()
