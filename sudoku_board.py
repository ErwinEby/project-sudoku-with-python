from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        rows = []
        for row in range(1, 10):
            blocks = [
                " ".join(str(self.sudoku[(row, column)]) for column in range(start, start + 3))
                for start in (1, 4, 7)
            ]
            rows.append("  ".join(blocks))
        return "\n\n".join(
            "\n".join(rows[start : start + 3])
            for start in (0, 3, 6)
        )

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            row, column, value = (argument.number for argument in symbol.arguments)
            sudoku[(row, column)] = value
        return cls(sudoku)
