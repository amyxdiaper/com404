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
        self.add_email_frame()
        self.add_email_entry()
        self.add_email_label()

        

    def add_heading_label(self):   
        #1. create the component object
        self.heading_label = Label()
        self.heading_label.pack(side = TOP)
        #2. style the component
        self.heading_label.configure(font="Arial 24", text="RECIEVE OUR NEWSLETTER")


    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.pack(side = TOP)
        self.instruction_label.configure (font="arial 12",
                                      text="Please enter your email below to recieve our newsletter.")

        
    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.pack(side = BOTTOM)
        self.subscribe_button.configure (width="65", text="subscribe")


    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side = RIGHT)
        self.email_entry.configure(width="35")


    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side = LEFT)
        self.email_label.configure(text="Email:")


        #creating a frame put inside brackets of function


    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
