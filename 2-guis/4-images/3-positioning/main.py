from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()


        # load images
        self.map_image_label = PhotoImage(file="map.gif")
        self.bus_image_label = PhotoImage(file="bus.gif")


        # set window attribuites
        self.title("Gui")

        # add components
        self.add_heading_label()
        self.add_map_frame()
        self.add_map_image_label()
        self.add_bus_image_label()


    def add_map_frame(self):
        self.map_frame = Frame(width=400, height=400)
        self.map_frame.place(x=0, y=0)


    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 20",
                                     text="Bus Journey")

    def add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)

        

    def add_bus_image_label(self):
        self.bus_image_label = Labell(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=bus_image)
        self.add_bus_image_label.bind("<B1-Motion>", self.button_clicked)
        
        

    # def bus_move(self, event):
         #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
         #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))

     #def button_clicked(self, event):
        




if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
