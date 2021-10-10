import unittest
import db


class Test_TestDB(unittest.TestCase):
    def test_add(self):
        db.init_db()
        save_move = ('p2', '0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0\nred 0 0 0 0 0 0', '', 'red', 'yellow', 41)
        db.add_move(save_move)
        load_move = db.getMove()
        self.assertEqual(save_move[0], load_move[0])


if __name__ == '__main__':
    unittest.main()