from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()


        # load images
        self.cactus_left_image = PhotoImage(file="cactus_left.gif")
        self.cactus_right_image = PhotoImage(file="cactus_right.gif")


        # set window attribuites
        self.title("Gui")

        # add components
        self.add_heading_label()
        self.add_cactus_image_label()
        self.add_flip_button()

        

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 20",
                                     text="Cactus Leaves")

    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_left_image,
                                               height=200,
                                               width=200)
    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(font="Arial 16",
                                   text="Flip")
        self.flip_button.bind("<ButtonRelease-1>", self.left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.right_button_clicked)


    def left_button_clicked(self, event):
        self.cactus_image_label.configure(image = self.cactus_left_image)

    def right_button_clicked(self, event):
        self.cactus_image_label.configure(image = self.cactus_right_image)




if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
