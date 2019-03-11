#Michael Freeman

from tkinter import *

class Game(Frame):
    """Mad Lib game."""
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text = "Let's play Mad Libs!").grid(row = 0, column = 0, sticky = W)
        #Create instruction label
        Label(self,
              text = "Fill in the missing bits:"
              ).grid(row = 1, column = 0, sticky = W)
        # create label for password
        self.pw_lbl1 = Label(self, text="Noun: ")
        self.pw_lbl1.grid(row=3, column=0, sticky=N)

        # password entry box
        self.noun_ent1 = Entry(self)
        self.noun_ent1.grid(row=3, column=1, sticky=N)

        # create label for password
        self.pw_lbl2 = Label(self, text="Noun: ")
        self.pw_lbl2.grid(row=4, column=0, sticky=N)

        # password entry box
        self.noun_ent2 = Entry(self)
        self.noun_ent2.grid(row=4, column=1, sticky=N)

        # create label for password
        self.pw_lbl3 = Label(self, text="Noun: ")
        self.pw_lbl3.grid(row=5, column=0, sticky=N)

        # password entry box
        self.noun_ent3 = Entry(self)
        self.noun_ent3.grid(row=5, column=1, sticky=N)

        #submit button
        self.submit_bttn = Button(self, text="Submit", command=self.tell_story)
        self.submit_bttn.grid(row=6, column=0, sticky=N)

        # create text widget to display message
        self.story_txt = Text(self, width=35, height=5, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=2, sticky=N)

    def tell_story(self):
        #Get values
        noun1 = self.noun_ent1.get()
        noun2 = self.noun_ent2.get()
        noun3 = self.noun_ent3.get()

        #Tell the story
        story = "You put in "
        story += noun1
        story += " And also "
        story += noun2
        story += " And finally"
        story += noun3

        #Display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Mad Libs!")

app = Game(root)

root.mainloop()