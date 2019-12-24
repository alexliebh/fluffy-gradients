from tkinter import *

class GradientWindow:

    def __init__(self, size, title):
        self.size = size
        self.title = title

        self.win = Tk()
        self.win.geometry(""+str(size[0])+"x"+str(size[1]))
        self.win.title(title)

    def show(self):
        self.win.mainloop()


