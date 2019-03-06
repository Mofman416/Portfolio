from tkinter import *

class Application(Frame):
    """GUI application that counts button clicks."""

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
    def create_widget(self):
        """Create button which displays number of clicks."""
        self.bttn = Button(self)
        lbl1 = Label(self, text = "Total Clicks:")
        lbl1.grid()
        lbl2 = Label(self, text = str(self.bttn_clicks))
        lbl2.grid()
        self.bttn["text"] = "Add a number."
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        self.bttn_clicks += 1
        self.lbl2["text"] = str(self.bttn_clicks)


root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()