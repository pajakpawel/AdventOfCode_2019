import unittest
from Day_1 import Puzzle_2


class TestSecondPuzzle(unittest.TestCase):
    def test_recursive_fuel_calculate(self):

        masses_with_solutions = (
            # A tuple of (mass, solution)
            (1, 0),
            (14, 2),
            (1969, 966),
            (100756, 50346),
        )

        for mass, solution in masses_with_solutions:
            with self.subTest("Recursive fuel correctness for given dataset", dataset=mass, solution=solution):
                self.assertEqual(Puzzle_2.recursive_fuel_calculate(mass), solution)

    def test_calculate_entire_fuel_required(self):

        datasets_with_solutions = (
            # A tuple of (dataset, solution)
            ([1], 0),
            ([14], 2),
            ([1969], 966),
            ([100756], 50346),
            ([14, 1969], 968),
            ([1, 14, 1969], 968),
        )

        for dataset, solution in datasets_with_solutions:
            with self.subTest("Entire fuel correctness for given dataset", dataset=dataset, solution=solution):
                self.assertEqual(Puzzle_2.calculate_entire_fuel_required(dataset), solution)


if __name__ == '__main__':
    unittest.main()
