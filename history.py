import os.path
import json, solve


class History:

    def check_file():
        if os.path.exists('history.json'):
            return True
        else:
            return False

    def entry_prep(unsolved, solved, solve_time):
        return {
            'puzzle': unsolved,
            'solution': solved,
            'time': solve_time
            }

    def save_puzzle(unsolved, solved, solve_time):
        history_file = 'history.json'
        # Read Json => Add history_entry to JSON => Save JSON
        history_data = History.read_history(history_file)
        history_entry = History.entry_prep(unsolved, solved, solve_time)
        History.write_history(history_file, history_data, history_entry)

    def write_history(history_file, history_data, history_entry, list_name='My List'):
        history_data[list_name].append(history_entry)
        new_history = json.dumps(history_data)
        with open(history_file, 'w') as f:
            f.write(new_history)
            print('Sudoku Saved!')

    def read_history(file):
        with open(file) as f:
            return json.loads(f.read())

    def input_list_name():
        return input('Enter List Name: ') or 'My List'

    def create_history(list_name, file='history.json'):
        with open(file, 'w+') as f:
            new_list = {list_name: []}
            f.write(json.dumps(new_list))

    def add_history(list_name, file='history.json'):
        pass

    def display_history(history_obj, list_name='My List'):
        history_item = history_obj[list_name]
        print(f'{list_name}\n')
        for item in history_item:
            print('Unsolved:\n')
            solve.Sudoku.display_board(item["puzzle"])
            print('Solved:\n')
            solve.Sudoku.display_board(item["solution"])
            print(f'Solved in {item["time"]} seconds\n')

            
            

