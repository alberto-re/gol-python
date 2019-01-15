#!/usr/bin/env python

import optparse
import logging
from random import seed
from tkinter import Tk, mainloop
from gol.game_state import GameState
from gol.board import Board


def parse_options():
    parser = optparse.OptionParser(usage="gol.py [OPTIONS]")
    parser.add_option("--grid-size",
                      action="store", dest="grid_size", default="50x50",
                      help="The grid's number of cells (default '20x20')")
    parser.add_option("--cell-size",
                      action="store", dest="cell_size", default="10",
                      help="The size in pixel of each cell (default '10')")
    parser.add_option("--density",
                      action="store", dest="density", default="0.15",
                      help="The probability of a cell to start as alive (default '0.15')")
    parser.add_option("--interval",
                      action="store", dest="interval", default="100",
                      help="The interval, in milliseconds, between each epoch (default '500')")
    parser.add_option("--seed",
                      action="store", dest="seed", default=None,
                      help="Sets a seed for RNG reproducibility")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    (options, args) = parse_options()
    rows, cols = map(int, options.grid_size.split("x"))
    cell_size = int(options.cell_size)
    density = float(options.density)
    interval = int(options.interval)
    if options.seed is not None:
        seed(int(options.seed))
    Tk()
    grid = GameState(rows, cols, density)
    canvas = Board(grid, cell_size, interval)
    canvas.run()
    mainloop()


if __name__ == "__main__":
    main()
