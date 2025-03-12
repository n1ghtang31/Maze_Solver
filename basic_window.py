import tkinter as tk
from tkinter import Tk, BOTH, Canvas

class Window(tk.Tk):
    def __init__(self, height, width):
        super().__init__()
        dimensions = f"{height}x{width}"
        self.geometry(dimensions)
        self.root = Tk()

win = Window(600, 400)

win.root.mainloop()