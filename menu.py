import PyInquirer as inq
import sys, solve, time, history


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
            unsolved = puzzle
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(unsolved, solution, solve_time)
        elif choice['Main Menu'] == choice_demo:
            puzzle = solve.Sudoku.demo
            unsolved = puzzle
            start_time = time.time()
            solution = solve.Sudoku.solve(puzzle)
            solve_time = f'{time.time() - start_time:.4f}'
            print(f'\nSolved in {solve_time} seconds.\n')
            Menu.solution_menu(unsolved, solution, solve_time)
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
            if history.History.check_file():
                # Save to File
                history.History.save_puzzle(puzzle, solution, solve_time)
            else:
                # Ask to set up file
                print('History file not found.')
                if Menu.file_not_found():
                    list_name = history.History.input_list_name()
                    history.History.create_history(list_name)
                    history.History.save_puzzle(puzzle, solution, solve_time)
                else:
                    Menu.solution_menu(puzzle, solution, solve_time)
        elif choice['Solution Menu'] == choice_again:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')
        elif choice['Solution Menu'] == choice_menu:
            print(f'PLACEHOLDER: {choice["Solution Menu"]}')

    def file_not_found():
        choice_yes = 'Yes'
        choice_no = 'No'

        options = [{
            'type': 'list',
            'name': 'No List Menu',
            'message': 'No List has been found?',
            'choices': [
                choice_yes,
                choice_no
            ]
        }]

        choice = inq.prompt(options)

        if choice['No List Menu'] == 'Yes':
            return True
        else:
            return False

    def return_menu():
        pass
