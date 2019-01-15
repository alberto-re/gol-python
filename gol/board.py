from tkinter import Canvas


class Board(Canvas):

    def __init__(self, grid, cell_size, interval):
        super().__init__(height=grid.n_rows*cell_size, width=grid.n_cols*cell_size)
        self._interval = interval
        self._cell_size = cell_size
        self._grid = grid

    def run(self):
        self.after(self._interval, self._update)
        self.pack()

    def _draw_state(self):
        for row in range(self._grid.n_rows):
            for col in range(self._grid.n_cols):
                if self._grid.cells[row][col] == 1:
                    self._draw_cell(row, col)

    def _draw_cell(self, row, col):
        x1 = col * self._cell_size
        y1 = row * self._cell_size
        x2 = x1 + self._cell_size
        y2 = y1 + self._cell_size
        self.create_rectangle(x1, y1, x2, y2, fill="black")

    def _update(self):
        self.delete("all")
        self._draw_state()
        self._grid.epoch()
        self.after(self._interval, self._update)
