from graphics import Window, Line, Point, Cell

def main():
    win = Window(1600, 900)
    line1 = Line(Point(100, 50), Point(400, 400))
   #win.draw_line(line1, "Green")
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell4 = Cell(win)
    cell1.has_bottom_wall = False
    cell4.has_top_wall = False
    cell1.draw(0, 0, 100, 100)
    cell2.draw(100, 0, 200, 100)
    cell3.draw(200, 0, 300, 100)
    cell4.draw(0, 100, 100, 200)
    win.wait_for_close()


main()