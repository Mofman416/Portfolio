from tkinter import *

class Application(Frame):
    """GUI application that counts button clicks."""

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Create an instruction label
        self.inst_lbl = Label(self, text = "Enter password for my Smash main.")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = N)# main
        # create label for password
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = N)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = N)

        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = N)

        #create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = N)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "shulk":
            message = "You got it!"
        else:
            message = "That is not the correct password, so I cannot share the secret with you."

        #Display the story
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)



root = Tk()
root.title("Secret Life")
root.geometry("300x150")

app = Application(root)

root.mainloop()
