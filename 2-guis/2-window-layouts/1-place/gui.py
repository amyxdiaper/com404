from tkinter import *



class Gui(Tk):


    #initilise the object
    def __init__(self):
        super().__init__()


        #set window attributes
        self.title("Gui")
        self.configure(bg="#eee", height=500, width=500)


        #add components/widgets
        self.add_heading_label()
        self.add_instruction_label()
        self.add_subscribe_button()
        self.add_email_entry()
        self.add_email_label()


    def add_heading_label(self):   
        #1. create the component object
        self.heading_label = Label()
        self.heading_label.place(x=20, y=10)
        #2. style the component
        self.heading_label.configure(font="Arial 24", text="RECIEVE OUR NEWSLETTER")


    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.place(x=50, y=100)
        self.instruction_label.configure (font="arial 12",
                                      text="Please enter your email below to recieve our newsletter.")

        

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.place(x=15, y=450)
        self.subscribe_button.configure (width="65", text="subscribe")


    def add_email_entry(self):
        self.email_entry = Entry()
        self.email_entry.place(x=150, y=350)
        self.email_entry.configure(width="35")


    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=100, y=350)
        self.email_label.configure(text="Email:")
