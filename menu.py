import PyInquirer as inq
import sys, solve, time
from history import History as history


class Menu:

    def start_menu():

        # Menu Choices
        choice_solve = 'Solve Sudoku'
        choice_demo = 'Run Demo'
        choice_history = 'View Saved Solutions'
        choice_exit = 'Exit'

        options = [{
            'type': 'list',
            'name': 'Main Menu',
            'message': 'What would you like to do?',
            'choices': [
                choice_solve,
                choice_demo,
                choice_history,
                choice_exit
            ]
        }]
        choice = inq.prompt(options)

        # Menu Logic
        if choice['Main Menu'] == choice_solve:
            puzzle = solve.Sudoku.input_puzzle()
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(puzzle, solution, solve_time)
        elif choice['Main Menu'] == choice_demo:
            puzzle = solve.Sudoku.demo
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(puzzle, solution, solve_time)
        elif choice['Main Menu'] == choice_history:
            print(f'PLACEHOLDER: {choice["Main Menu"]}')
        elif choice['Main Menu'] == choice_exit:
            sys.exit()

    def solution_menu(puzzle, solution, solve_time):
        choice_save = 'Save Puzzle and Solution'
        choice_again = 'Solve another puzzle'
        choice_menu = 'Back to Main Menu'

        options = [{
            'type': 'list',
            'name': 'Solution Menu',
            'message': 'What would you like to do?',
            'choices': [
                choice_save,
                choice_again,
                choice_menu
            ]
        }]
        choice = inq.prompt(options)

        if choice['Solution Menu'] == choice_save:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')
            if history.check_file:
                # Save to File
                pass
            else:
                # Ask to set up file
                pass
        elif choice['Solution Menu'] == choice_again:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')
        elif choice['Solution Menu'] == choice_menu:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')

    def return_menu():
        pass
