import PyInquirer as inq
import sys

class Menu:

    def start_menu():
        options = [{
            'type': 'list',
            'name': 'Main Menu',
            'message': 'What would you like to do?',
            'choices': [
                'Solve Sudoku',
                'View Saved Solutions',
                'Exit'
            ]
        }]
        choice = inq.prompt(options)
        if choice['Main Menu'] == 'Solve Sudoku':
            print(f'PLACEHOLDER: {choice["Main Menu"]}')
        elif choice['Main Menu'] == 'View Saved Solutions':
            print(f'PLACEHOLDER: {choice["Main Menu"]}')
        elif choice['Main Menu'] == 'Exit':
            sys.exit()

    def return_menu():
        pass