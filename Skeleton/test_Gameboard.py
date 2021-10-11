import unittest
from Gameboard import Gameboard


class Test_TestGamemboard(unittest.TestCase):

    def setUp(self):
        self.game = Gameboard()

    def tearDown(self):
        self.game = None

    def test_validate_move(self):
        self.assertEqual(self.game.validate_move("p1", 0), "No color chosen")
        self.game.player1 = "red"
        self.assertEqual(self.game.validate_move("p1", 0), "No color chosen")
        self.game.player2 = "yellow"
        self.assertEqual(self.game.validate_move("p2", 0), "Not your turn")
        self.assertEqual(self.game.validate_move("p1", 8), "Out of Bounds")
        self.assertEqual(self.game.validate_move("p1", 0), "Valid")
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.validate_move("p1", 0), "Not your turn")
        self.game.add_chip("p2", 0)
        self.game.add_chip("p1", 0)
        self.game.add_chip("p2", 0)
        self.game.add_chip("p1", 0)
        self.game.add_chip("p2", 0)
        self.game.add_chip("p1", 0)
        self.game.add_chip("p2", 0)
        self.assertEqual(self.game.validate_move("p1", 0), "Overflow")
        self.game.remaining_moves = 0
        self.assertEqual(self.game.validate_move("p1", 0), "Out of Moves")
        self.game.game_result = "p1"
        self.assertEqual(self.game.validate_move("p1", 0), "End Of Game")

    def test_add_chip(self):
        self.game.player1 = "yellow"
        self.game.player2 = "red"
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.board[5][0], "p1")
        self.game.add_chip("p2", 0)
        self.assertEqual(self.game.board[4][0], "p2")
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.board[3][0], "p1")
        self.game.add_chip("p2", 0)
        self.assertEqual(self.game.board[2][0], "p2")
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.board[1][0], "p1")
        self.game.add_chip("p2", 0)
        self.assertEqual(self.game.board[0][0], "p2")
        self.assertEqual(self.game.remaining_moves, 36)

    def test_check_row(self):
        self.game.add_chip("p1", 0)
        self.game.add_chip("p1", 1)
        self.game.add_chip("p1", 2)
        self.assertEqual(self.game.check_row("p1", 5), False)
        self.assertEqual(self.game.check_row("p2", 5), False)
        self.game.add_chip("p1", 5)
        self.assertEqual(self.game.check_row("p1", 5), False)
        self.game.add_chip("p1", 3)
        self.assertEqual(self.game.check_row("p1", 5), True)
        self.assertEqual(self.game.check_row("p2", 5), False)

    def test_check_col(self):
        self.game.add_chip("p1", 0)
        self.game.add_chip("p2", 0)
        self.assertEqual(self.game.check_col("p2", 0), False)
        self.game.add_chip("p1", 0)
        self.game.add_chip("p1", 0)
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.check_col("p1", 0), False)
        self.game.add_chip("p1", 0)
        self.assertEqual(self.game.check_col("p1", 0), True)

    def test_check_pdaig(self):
        self.game.board[5][0] = "p1"
        self.game.board[4][1] = "p2"
        self.assertEqual(self.game.check_pdiag("p2", 1, 4), False)
        self.game.board[3][2] = "p1"
        self.game.board[2][3] = "p1"
        self.game.board[1][4] = "p1"
        self.assertEqual(self.game.check_pdiag("p1", 4, 1), False)
        self.game.board[0][5] = "p1"
        self.assertEqual(self.game.check_pdiag("p1", 5, 0), True)

    def test_check_ndaig(self):
        self.game.board[5][5] = "p1"
        self.game.board[4][4] = "p2"
        self.assertEqual(self.game.check_ndiag("p2", 4, 4), False)
        self.game.board[3][3] = "p1"
        self.game.board[2][2] = "p1"
        self.game.board[1][1] = "p1"
        self.assertEqual(self.game.check_ndiag("p1", 1, 1), False)
        self.game.board[0][0] = "p1"
        self.assertEqual(self.game.check_ndiag("p1", 0, 0), True)


if __name__ == '__main__':
    unittest.main()
