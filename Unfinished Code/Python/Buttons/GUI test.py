from tkinter import *

class Application(Frame):
    """GUI Application, with classes!"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text = "Choose you favorite movie types.").grid(row = 0, column = 0, sticky = W)
        #Create instruction label
        Label(self,
              text = "Select all that apply:"
              ).grid(row = 1, column = 0, sticky = W)

        ##creates Comedy check button.
#        self.likes_comedy = BooleanVar()
        #        Checkbutton(self,
        #           text = "Comedy",
        #           variable = self.likes_comedy,
        #           command = self.update_text
        #           ).grid(row = 2, column = 0, sticky = W)
        #
        ## creates Drama check button.
        #self.likes_drama = BooleanVar()
        #Checkbutton(self,
        #           text = "Drama",
        #           variable = self.likes_drama,
        #           command = self.update_text
        #           ).grid(row = 3, column = 0, sticky = W)
        #
        ## creates Romance check button.
        #self.likes_romance = BooleanVar()
        #Checkbutton(self,
        #           text = "Romance",
        #           variable = self.likes_romance,
        #           command = self.update_text
        #           ).grid(row = 4, column = 0, sticky = W)

        self.favorite = StringVar()
        self.favorite.set(None)

        #create Comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "Comedy.",
                    command = self.update_text()
                    ).grid(row = 2, colimn = 0, sticky = W)

        # create Drama radio button
        Radiobutton(self,
                    text="Drama",
                    variable=self.favorite,
                    value="Drama.",
                    command=self.update_text()
                    ).grid(row=2, colimn=0, sticky=W)

        # create Romance radio button
        Radiobutton(self,
                    text="Romance",
                    variable=self.favorite,
                    value="Romance.",
                    command=self.update_text()
                    ).grid(row=2, colimn=0, sticky=W)

        #create text field to display results
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        # """Update text widget and display user's favorite movie types."""
        # likes = ""
        # if self.likes_comedy.get():
        #     likes += "You like comedic movies.\n"
        #
        # if self.likes_drama.get():
        #     likes += "You like dramatic movies.\n"
        #
        # if self.likes_romance.get():
        #     likes += "You like romantic movies.\n"
        # self.results_txt.delete(0.0,END)
        # self.results_txt.insert(0.0, likes)

        message = "Your favorite type of movie is "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


root = Tk()
root.title("Test")
root.geometry("200x85")

app = Application(root)
root.mainloop()