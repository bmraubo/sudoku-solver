import PyInquirer as inq
import sys
import solve
import time


class Menu:

    def start_menu():

        # Menu Choices
        choice1 = 'Solve Sudoku'
        choice2 = 'Run Demo'
        choice3 = 'View Saved Solutions'
        choice_exit = 'Exit'

        options = [{
            'type': 'list',
            'name': 'Main Menu',
            'message': 'What would you like to do?',
            'choices': [
                choice1,
                choice2,
                choice3,
                choice_exit
            ]
        }]
        choice = inq.prompt(options)

        # Menu Logic
        if choice['Main Menu'] == choice1:
            puzzle = solve.Sudoku.input_puzzle()
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(puzzle, solution, solve_time)
        elif choice['Main Menu'] == choice2:
            puzzle = solve.Sudoku.demo
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(puzzle, solution, solve_time)
        elif choice['Main Menu'] == choice3:
            print(f'PLACEHOLDER: {choice["Main Menu"]}')
        elif choice['Main Menu'] == choice_exit:
            sys.exit()

    def solution_menu(puzzle, solution, solve_time):
        choose_history = 'Save Puzzle and Solution'
        choose_again = 'Solve another puzzle'
        choose_menu = 'Back to Main Menu'

        options = [{
            'type': 'list',
            'name': 'Solution Menu',
            'message': 'What would you like to do?',
            'choices': [
                choose_history,
                choose_again,
                choose_menu
            ]
        }]
        choice = inq.prompt(options)

        if choice['Solution Menu'] == choose_history:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')
        elif choice['Solution Menu'] == choose_again:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')
        elif choice['Solution Menu'] == choose_menu:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')

    def return_menu():
        pass
