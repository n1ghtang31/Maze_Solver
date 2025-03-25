import time
import random
from graphics import Cell, Point, Line
class Maze:
    def __init__(
            self,
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win = None, 
            seed=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.seed = seed
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

        if self.seed is not None:
            self.seed = random.seed(seed)

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
        if self._win is None:
            return
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
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.08)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0,0)
        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cells(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            need_to_visit = []

            # Search to the right
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                need_to_visit.append((i+1, j))
            # Search bottom
            if j < self.num_rows -1 and not self._cells[i][j+1].visited:
                need_to_visit.append((i,j+1))
            # Search left
            if i > 0 and not self._cells[i-1][j].visited:
                need_to_visit.append((i-1,j))
            # Search top
            if j > 0 and not self._cells[i][j-1].visited:
                need_to_visit.append((i,j-1))

            if not need_to_visit:
                self._draw_cells(i, j)
                return
            
            direction = random.randrange(len(need_to_visit))
            next_cell = need_to_visit[direction]
            
            # Break to right
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_cell[0], next_cell[1])

