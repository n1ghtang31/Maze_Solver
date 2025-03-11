from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.root = Tk()

win = Window(600, 400)

win.root.mainloop()