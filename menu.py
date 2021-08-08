import PyInquirer as inq
import sys
import solve


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
        if choice['Main Menu'] == choice1:
            puzzle = solve.Sudoku.input_puzzle()
            solve.Sudoku.solve(puzzle)
        elif choice['Main Menu'] == choice2:
            puzzle = solve.Sudoku.demo
            solve.Sudoku.solve(puzzle)
        elif choice['Main Menu'] == choice3:
            print(f'PLACEHOLDER: {choice["Main Menu"]}')
        elif choice['Main Menu'] == choice_exit:
            sys.exit()

    def return_menu():
        pass
