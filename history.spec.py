import unittest
import history

test_sudoku = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]

test_solution = [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]

test_solve_time = '0.005'


class HistoryTests(unittest.TestCase):

    def test_entry_prep(self):
        self.assertEqual(history.History.entry_prep(
                        test_sudoku, test_solution, test_solve_time),
                        {
                        'puzzle': test_sudoku,
                        'solution': test_solution,
                        'time': test_solve_time
                        })

    def test_read(self):
        file = 'test.json'
        test_history = history.History.entry_prep(
                                        test_sudoku, 
                                        test_solution, 
                                        test_solve_time
                                        )
        history_check = history.History.read_history(file)
        self.assertEqual(history_check[0], test_history)

    def test_write(self):
        file = 'test.json'
        test_history = history.History.entry_prep(
                                        test_sudoku,
                                        test_solution,
                                        test_solve_time
                                        )
        history_data = history.History.read_history(file)
        history.History.write_history(file, history_data, test_history)
        history_check = history.History.read_history(file)
        self.assertEqual(history_check[-1], test_history)

    def test_display(self):
        pass

unittest.main()