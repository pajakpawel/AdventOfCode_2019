import unittest
from Day_1 import Puzzle_1


class TestFirstPuzzle(unittest.TestCase):
    def test_count_fuel_required(self):

        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583),
            ({12, 14}, 4),
            ({12, 14, 1969}, 658)
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Solution correctness for given dataset", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_1.count_fuel_required(dataset), solution)


if __name__ == '__main__':
    unittest.main()
