import unittest
from day04 import get_col, get_loser, get_row, getInput, getLoser, getWinner, getScore
from __fixtures__.parsedTestInput import numbers, boards


class GetInputTestCases(unittest.TestCase):
    def test_parses_test_input(self):
        self.assertEqual(getInput('test-input.txt'), (numbers, boards))

    def test_parses_input(self):
        self.assertEqual(getInput('input.txt'), False)


class GetWinnerTestCases(unittest.TestCase):
    def test_gets_test_winner(self):
        self.assertEqual(getWinner(numbers, boards), (boards[2], numbers[:12]))

    def test_gets_winner(self):
        self.assertEqual(getWinner(numbers, boards), -1)


class GetScoreTestCases(unittest.TestCase):
    def test_gets_test_score(self):
        self.assertEqual(getScore(boards[2], numbers[:11+1]), 4512)


class GetColRowTestCases(unittest.TestCase):
    def test_get_row(self):
        self.assertEqual(get_row(boards[0], 0), [22, 13, 17, 11, 0, ])
        self.assertEqual(get_row(boards[0], 3), [22, 13, 17, 11, 0, ])
        self.assertEqual(get_row(boards[0], 15), [6, 10, 3, 18, 5, ])
        self.assertEqual(get_row(boards[0], 24), [1, 12, 20, 15, 19])

    def test_get_col(self):
        self.assertEqual(get_col(boards[1], 0), [3, 9, 19, 20, 14])
        self.assertEqual(get_col(boards[1], 4), [22, 5, 23, 4, 6])
        self.assertEqual(get_col(boards[1], 6), [15, 18, 8, 11, 21])
        self.assertEqual(get_col(boards[1], 24), [22, 5, 23, 4, 6])
        self.assertEqual(get_col(boards[1], 17), [0, 13, 7, 10, 16])


class GetLoserTestCases(unittest.TestCase):
    def test_get_loser_testinput(self):
        getLoser(numbers, boards)
