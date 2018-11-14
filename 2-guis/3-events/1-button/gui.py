
from tkinter import *

class Gui(Tk):

    # constructor - initialises the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("My Gui")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        # add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_tickets_entry()
        self.add_submit_button()
        

    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0)
        # style
        self.heading_label.configure(font="Arial 22",
                                     text="Entrance Ticket")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=2, column=0)
        self.instruction_label.configure(font="Arial 16",
                                         text="How many tickets are needed?")

        

    def add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=3, column=0)
        self.tickets_entry.configure(width=30)
        
        
    

    def add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.grid(row=4, column=0)
        self.submit_button.configure(width=40,
                                     font="Arial 12",
                                     text="Submit")
        # bind events
        
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

    def submit_button_clicked(self, event):
        num_tickets = self.tickets_entry.get()
        messagebox.showinfo("Gui", "You have purchased " + num_tickets + " tickets!")
        
    
        

        
        
        
        
        
        
        
        
        
        
        
        
inter import *

class Gui(Tk):

    # constructor - initialises the object
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("My Gui")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        # add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_entry()
        self.add_subscribe_button()
        

    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.grid(row=1, column=0)
        # style
        self.heading_label.configure(font="Arial 22",
                                     text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=2, column=0)
        self.instruction_label.configure(font="Arial 16",
                                         text="Please enter your email below to receive our newsletter.")


    def add_email_label(self):
        self.email_label = Label()
        self.email_label.grid(row=3, column=0)
        self.email_label.configure(font="Arial 14",
                                   text="Email")

        

    def add_email_entry(self):
        self.email_entry = Entry()
        self.email_entry.grid(row=4, column=0)
        self.email_entry.configure(width=30)
        
        
    

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=5, column=0)
        self.subscribe_button.configure(width=40,
                                     font="Arial 14",
                                     text="Submit")
        # bind events
        
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    def subscribe_button_clicked(self, event):
        user_email = self.email_entry.get()
        messagebox.showinfo("Gui", "Your email " + user_email + " has been added.")
        
    
        
        
        
        
        
        
