from tkinter import *

class Gui(Tk):

    # constructor - initialises the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("My Gui")
        self.configure(bg="#f00",
                       height=500,
                       width=500)

        # add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()
        

    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        # style
        self.heading_label.configure(font="Arial 16",
                                     text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, columnspan=2)
        self.instruction_label.configure(font="Arial 12",
                                         text="Please enter your email below to recieve our newsletter.")
        

    def add_email_label(self):
        self.email_label = Label()
        self.email_label.grid(row=2, column=0, columnspan=1)
        self.email_label.configure(font="Arial 11",
                                   text="Email")
        

    def add_email_entry(self):
        self.email_entry = Entry()
        self.email_entry.grid(row=2, column=1, columnspan=1)
        self.email_entry.configure(width=50)                       
    

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=3, column=0, columnspan=2)
        self.subscribe_button.configure(font="Arial 11",
                                        text="Subscribe",
                                        width=50)
