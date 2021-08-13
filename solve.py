class Sudoku:

    demo = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    def solve(puzzle):
        Sudoku.display_board(puzzle)
        puzzle = Sudoku.next_value(puzzle)
        Sudoku.display_board(puzzle)
        return puzzle

    # Displaying the board
    def display_board(puzzle):
        print('\n')
        print('+-------+-------+-------+')
        for y in range(0, len(puzzle)):
            print(f'| {puzzle[y][0]} {puzzle[y][1]} {puzzle[y][2]} ' +
                    f'| {puzzle[y][3]} {puzzle[y][4]} {puzzle[y][5]} ' +
                    f'| {puzzle[y][6]} {puzzle[y][7]} {puzzle[y][8]} |')
            if y in [2, 5, 8]:
                print('+-------+-------+-------+')

    # Input Puzzle

    def convert_row(row):
        converted_row = []
        for num in row:
            converted_row.append(int(num))
        return converted_row

    def validate_row(row, puzzle):
        if len(row) < 9:
            print('Ooops! - Row too short!!!')
            return False
        elif len(row) > 9:
            print('Ooops! - Row too long!!!')
            return False
        Sudoku.display_board(puzzle)
        answer = input('Is that correct? y/n ')
        if answer.lower() == 'y':
            return True
        else:
            return False

    def input_puzzle():
        puzzle = []
        input_msg = 'Input the known values.\nIf value is blank, input 0.\nEg. 530070000\n'
        while len(puzzle) < 9:
            valid = False
            while not valid:
                new_row = input(input_msg)
                puzzle.append(Sudoku.convert_row(new_row))
                valid = Sudoku.validate_row(new_row, puzzle)
                if not valid:
                    puzzle.pop()
                    print('Try Again\n\n')
        return puzzle

    # Solution Logic
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
