
import numpy


class Sudoku:

    def solve(puzzle):
        print(numpy.matrix(puzzle), '\n')
        puzzle = Sudoku.next_value(puzzle)
        print(numpy.matrix(puzzle))
        return puzzle

    def next_value(puzzle):
        for y in range(0, 9):
            for x in range(0, 9):
                if puzzle[y][x] == 0:
                    for n in range(1, 10):
                        if Sudoku.poss(puzzle, x, y, n):
                            puzzle[y][x] = n
                            if Sudoku.next_value(puzzle):
                                return puzzle
                            puzzle[y][x] = 0
                    return
        return puzzle

    def poss(puzzle, x, y, n):
        # for n checks against nums in x,y axis to see if num is possible
        for col in range(0, 9):
            if puzzle[y][col] == n:
                return False
        for row in range(0, 9):
            if puzzle[row][x] == n:
                return False
        # for n checks 3x3 square to see if it is possible
        x_sq = (x//3)*3
        y_sq = (y//3)*3
        for a in range(0, 3):
            for b in range(0, 3):
                if puzzle[y_sq+a][x_sq+b] == n:
                    return False
        # if n does not match any number, returns True
        return True
