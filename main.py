from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    num_rows = 15
    num_cols = 15
    margin = 50
    screen_x = 1600
    screen_y = 900
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 *margin) / num_rows
   
    win = Window(1600, 900)
   
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()