from typing import List

GridType = type(List[List[int]])


class Sudoku:

    def __init__(self):
        self.grid: GridType = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        self.changed: bool = False
        self.completed: bool = False

    def render_grid(self) -> None:
        print("-------------------------------")
        for i, row in enumerate(self.grid):
            text_to_print = '|'
            for j, digit in enumerate(row):
                text_to_print += f' {str(digit)} '
                if (j + 1) % 3 == 0:
                    text_to_print += '|'
            print(text_to_print)
            if (i + 1) % 3 == 0:
                print("-------------------------------")

    def get_block_integer_list(self, x, y) -> List[int]:
        digit_list = []
        for i in range(3):
            for j in range(3):
                digit_list.append(self.grid[i + ((x // 3) * 3)][j + ((y // 3) * 3)])

        return digit_list


    def enterNumberIfPossible(self, x, y) -> None:
        already_used_number_list: List[int] = []
        for digit in self.grid[x]:
            if digit != 0:
                try:
                    already_used_number_list.index(digit)
                except ValueError:
                    already_used_number_list.append(digit)

        for i in range(0, 9):
            if self.grid[i][y] != 0:
                try:
                    already_used_number_list.index(self.grid[i][y])
                except ValueError:
                    already_used_number_list.append(self.grid[i][y])

        for digit in self.get_block_integer_list(x, y):
            if digit != 0:
                try:
                    already_used_number_list.index(digit)
                except ValueError:
                    already_used_number_list.append(digit)

        if len(already_used_number_list) == 8:
            self.changed = True
            for i in range(1, 10):
                try:
                    already_used_number_list.index(i)
                except ValueError:
                    self.grid[x][y] = i

    def check_if_solved(self) -> bool:
        for rows in self.grid:
            for digit in rows:
                if digit == 0:
                    return False
        return True

    def solve_sudoku(self) -> GridType:
        while not self.completed:
            self.changed = False
            for x, row in enumerate(self.grid):
                for y, digit in enumerate(row):
                    if digit == 0:
                        self.enterNumberIfPossible(x, y)
            if not self.changed and self.check_if_solved():
                self.completed = True
        self.render_grid()
        return self.grid


sudoku = Sudoku()

sudoku.solve_sudoku()
