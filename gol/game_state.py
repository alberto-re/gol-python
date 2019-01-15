import logging
from copy import deepcopy
from random import random


class GameState:

    def __init__(self, rows=40, cols=60, density=0.15, array=None):
        self._epoch = 0
        if array is not None:
            self._n_rows = len(array)
            self._n_cols = len(array[0])
            self._cells = deepcopy(array)
        else:
            self._n_rows = rows
            self._n_cols = cols
            self._cells = [[1 if random() <= density else 0 for _ in range(0, cols)]
                           for _ in range(0, rows)]
        logging.info("Initiated Grid with shape %dx%d" % (self._n_rows, self._n_cols))

    def epoch(self):
        next_epoch = deepcopy(self._cells)
        self._epoch += 1
        logging.info("Computing epoch %d" % self._epoch)
        for col in range(self.n_cols):
            for row in range(self.n_rows):
                neighbors = self._neighbors_score(row, col)
                if next_epoch[row][col] == 1:
                    if neighbors < 2 or neighbors > 3:
                        next_epoch[row][col] = 0
                else:
                    if neighbors == 3:
                        next_epoch[row][col] = 1
        self._cells = next_epoch

    def _neighbors_score(self, row, col):
        up = row - 1
        right = 0 if col == self._n_cols - 1 else col + 1
        left = col - 1
        down = 0 if row == self._n_rows - 1 else row + 1
        return self._cells[up][left] + self._cells[up][col] + self._cells[up][right] \
            + self._cells[row][left] + self._cells[row][right] + self._cells[down][left] \
            + self._cells[down][col] + self._cells[down][right]

    @property
    def cells(self):
        return self._cells

    @property
    def n_rows(self):
        return self._n_rows

    @property
    def n_cols(self):
        return self._n_cols
