import time
from graphics import Cell
class Maze:
    def __init__(
            self,
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win, 
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        # Create a matrix of cells
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                c = Cell(self._win)
                col.append(c)
            self._cells.append(col)

        for i, row in enumerate(self._cells):
            for j, cells in enumerate(row):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        current_cell = self._cells[i][j]
        start_x = self.x1
        start_y = self.y1
        increment_x = self.cell_size_x
        increment_y = self.cell_size_y
        x1 = (increment_x * i) + start_x
        y1 = (increment_y * j) + start_y
        x2 = (increment_x * (i+1)) + start_x
        y2 = (increment_y * (j+1)) + start_y

        current_cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)



