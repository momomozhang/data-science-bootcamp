import unittest

from functions import PLAYER_O, PLAYER_X, is_full_board, win_check


class TestIsFull(unittest.TestCase):
    def test_full_board_returns_true(self):
        board_full = {
            "A1": PLAYER_X,
            "A2": PLAYER_O,
            "A3": PLAYER_X,
            "B1": PLAYER_O,
            "B2": PLAYER_X,
            "B3": PLAYER_O,
            "C1": PLAYER_X,
            "C2": PLAYER_O,
            "C3": PLAYER_X,
        }

        result = is_full_board(board_full)
        self.assertTrue(result)

    def test_empty_board_returns_false(self):
        board_empty = {
            "A1": "A1",
            "A2": "A2",
            "A3": "A3",
            "B1": "B1",
            "B2": "B2",
            "B3": "B3",
            "C1": "C1",
            "C2": "C2",
            "C3": "C3",
        }

        result = is_full_board(board_empty)
        self.assertFalse(result)

    def test_half_empty_board_returns_false(self):
        board_half_empty = {
            "A1": PLAYER_X,
            "A2": "A2",
            "A3": "A3",
            "B1": "B1",
            "B2": "B2",
            "B3": "B3",
            "C1": "C1",
            "C2": "C2",
            "C3": "C3",
        }

        result = is_full_board(board_half_empty)
        self.assertFalse(result)


class TestWinCheck(unittest.TestCase):
    def test_win_returns_true(self):
        board_win = {
            "A1": PLAYER_X,
            "A2": PLAYER_X,
            "A3": PLAYER_X,
            "B1": PLAYER_O,
            "B2": "B2",
            "B3": PLAYER_O,
            "C1": PLAYER_O,
            "C2": "C2",
            "C3": "C3",
        }

        result = win_check(board_win)
        self.assertTrue(result)

    def test_draw_returns_false(self):
        board_draw = {
            "A1": PLAYER_X,
            "A2": PLAYER_O,
            "A3": PLAYER_X,
            "B1": PLAYER_X,
            "B2": PLAYER_O,
            "B3": PLAYER_O,
            "C1": PLAYER_O,
            "C2": PLAYER_X,
            "C3": PLAYER_X,
        }

        result = win_check(board_draw)
        self.assertFalse(result)

    def test_not_finish_returns_false(self):
        board_not_finish = {
            "A1": PLAYER_X,
            "A2": "A2",
            "A3": PLAYER_X,
            "B1": PLAYER_X,
            "B2": PLAYER_O,
            "B3": PLAYER_O,
            "C1": PLAYER_O,
            "C2": "C2",
            "C3": PLAYER_X,
        }
        result = win_check(board_not_finish)
        self.assertFalse(result)
