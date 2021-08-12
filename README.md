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

# August Additions

So, now that the sudoku algo is in place, it would be nice to make it usable. I want to add a couple of things:

- Making it pretty - give the display of the puzzles some love
- System for inputting sudokus you find online/in RL.
- Ability to store puzzles (and solutions)
- Ability to have a little demo mode
- Display how long it took to find the solution.
- and a menu system to tie it all together.

## Making it pretty

First thing I touched - just a small function Sudoku.display_board() to print out the information in a visually pleasing manner based on an example I found through Google Image search. 

The way the func is designed allows for partial boards to be printed - this was kind of accidental but helps with the feedback of information when inputting the board - see below.

## Puzzle Input

So in an ideal world, I would just want to be able to take a picture of a sudoku, or screenshot, and have that be solved. But that is a little beyond me for now.

Instead, I used an input function that asks you to type in the puzzle row by row, with 0 reprepresenting missing values. It is not the most graceful solution perhaps, but it does allow me to quite easily feed in the input into the solution fucntion.

The one thing I regret is having to validate each row after it is typed. It is very annoying because most of the time I got the row right, and repeatedly validating got tedious. Then again, when a mistake is made, it mean not only having to start the puzzle again, but also having to complete input of any further rows. Which would be really shit. So its a judgment call between a small amount of constant annoyance or rare catastrophies. Hmmm.

You can't even press Enter several times... that will just register the row as incomplete. Perhaps it should recognise that if youre just tapping Enter, you've given up on the process. 

## Storing Puzzles

Haven't touched that yet, but just write puzzle and solution to JSON

## Demo mode

Demo Mode is simple enough - it allows the functionality of the solver to be shown off using a pre-determined puzzle, instead of going through the labour intensive process of finding a Sudoku and inputting it into the program line by line.
