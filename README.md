# sudoku-solver

Sudoku Solver - experimenting with Atom

Nothing fancy, just a sudoku solver based on the tutorial by [ComputerPhile](#https://www.youtube.com/watch?v=G_UYXzGuqvM). Built test first using unittest. As a result, instead of just printing a value, it returns it - it can therefore be incorporated into other code.

At the heart of the software lies a recursive algorithm, that I'm going to talk about to crystalise my thinking:

```
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
```

What it does: goes through each list in the array and when it hits a zero, it replaces it with the first possible number (checked using the poss function).

Then next_value() calls itself, and so the process continues until it encounters a '0' with no possible solution - it then backtracks - returns through the layers of the function until it reaches a point where more than one value is possible, and proceeds as above with the next possible value.

This is where the code diverges from ComputerPhile's tutorial:

```
if Sudoku.next_value(puzzle):
    return puzzle
```

This passes up the answer from the last run of the recursive function to the allow the final `return puzzle` to provide us with a solution, rather than 'None'.

The poss function is simple enough - it checks a input value against the rows and columns according to the rules of Sudoku. The more complicated aspect of these checks are the 3x3 squares. This is dealt with as follows (I take no credit for it - its from ComputerPhile):

```
x_sq = (x//3)*3
y_sq = (y//3)*3
for a in range(0, 3):
    for b in range(0, 3):
        if puzzle[y_sq+a][x_sq+b] == n:
            return False
```

The // operator is Floor Division. It returns full values, so 3//3 == 1, but 2//3 == 0. This allows squares to be defined - the first three checks will all floor divide to 0, so script can check through all and only the values in the 3x3 square.

Will be working on an input function that will allow quick entry of any puzzle.

A nice interface showing the puzzle being solved would be good to look into - tutorials exist for this.
