﻿from tkinter import *
from PIL import ImageTk

class GradientWindow:

    def __init__(self, size, title):
        self.size = size
        self.title = title

        self.win = Tk()
        self.win.geometry(""+str(size[0])+"x"+str(size[1]))
        self.win.title(title)
        self.canvas = Canvas(self.win, width=self.size[0], height=self.size[1]-100, bg="red")
        self.canvas.pack()


        self.image = None
        self.imageCounter = 0


    def set_image(self, img):
        self.image = img

        photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(250, 250, image=photo)
        self.canvas.place(width=self.size[0], height=self.size[1]-100)
        self.win.mainloop()
