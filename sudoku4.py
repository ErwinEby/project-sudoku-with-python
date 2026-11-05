import sys
import clingo
from clingo.application import Application, clingo_main

from sudoku_board import Sudoku

SUDOKU_ENCODING = r"""
num(1..9).

1 { sudoku(X,Y,N) : num(N) } 1 :- num(X), num(Y).
sudoku(X,Y,N) :- initial(X,Y,N).

:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 < Y2.
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 < X2.

subgrid(X,Y,((X-1)/3)*3 + ((Y-1)/3) + 1) :- num(X), num(Y).

:- sudoku(X1,Y1,N), sudoku(X2,Y2,N),
   subgrid(X1,Y1,G), subgrid(X2,Y2,G),
   (X1,Y1) < (X2,Y2).

#show sudoku/3.
"""


class SudokuApp(Application):
    def print_model(self, model: clingo.solving.Model, printer) -> None:
        print(Sudoku.from_model(model))
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.add("base", [], SUDOKU_ENCODING)
        for path in files:
            ctl.load(path)
        ctl.ground([("base", [])])
        ctl.solve()


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])
