import tkinter as tk
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("This is the title for the Maze Solver")
        self.__canvas = tk.Canvas(
            self.__root,
            width=width,
            height=height,
            bg="white"
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.....")
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x} Y: {self.y}"
        
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, _win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = _win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        
    def draw_move(self, to_cell, undo=False):
        center_from = self.find_center()
        from_canvas = self._win
        center_to = to_cell.find_center()
        travel_line = Line(center_from, center_to)
        if undo == True:
            from_canvas.draw_line(travel_line, fill_color="red")
        else:
            from_canvas.draw_line(travel_line, fill_color="gray")

    def find_center(self):
        # So to find center you need to minus x2 - x1 divide by 2 then adde to x1 repeat for y-coords        
        minus_x = abs(self._x2 - self._x1)      
        divide_x = minus_x // 2
        add_x = divide_x + self._x1

        minus_y = abs(self._y2 - self._y1)      
        divide_y = minus_y // 2
        add_y = divide_y + self._y1
        return Point(add_x, add_y)