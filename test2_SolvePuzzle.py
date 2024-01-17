from SolvePuzzle import solve_puzzle
import unittest


class TestSolvePuzzle(unittest.TestCase):
    def test_dosctrings(self):
        """Searches for docstrings"""
        self.assertIsNotNone(solve_puzzle.__doc__, "solve_puzzle needs a docstring")

    def setUp(self):
        """A few boards for testing"""
        # Note - there may be multiple optimal paths, but the number of moves is fixed.
        # We only test the number of moves.
        # One possible optimal path for each board is provided for debugging purposes.
        self.board0, self.opt_path0, self.opt_moves0 = [8, 8, 4, 2, 1, 9, 7, 4, 4, 6], [0, 8, 4, 3, 1, 9], 5
        self.board1, self.opt_path1, self.opt_moves1 = [8, 9, 0, 1, 5, 10, 3, 3, 2, 7], [0, 8, 6, 9], 3
        self.board2, self.opt_path2, self.opt_moves2 = [8, 4, 3, 5, 2, 4, 3, 1, 2, 4], [0, 8, 6, 9], 3
        self.board3, self.opt_path3, self.opt_moves3 = [5, 9, 2, 6, 8, 2, 2, 9, 10, 3], [0, 5, 3, 9], 3
        self.board4, self.opt_path4, self.opt_moves4 = [4, 3, 1, 6, 2, 0, 2, 3, 3, 4], [0, 4, 2, 3, 9], 4
        self.board5, self.opt_path5, self.opt_moves5 = [2, 8, 1, 8, 4, 7, 1, 6, 9, 7], [0, 2, 1, 9], 3
        self.board6, self.opt_path6, self.opt_moves6 = [6, 8, 2, 3, 5, 3, 4, 5, 7, 9], [0, 6, 2, 4, 9], 4
        self.board7, self.opt_path7, self.opt_moves7 = [7, 7, 7, 5, 3, 1, 8, 5, 1, 2], [0, 7, 2, 9], 3
        self.board8, self.opt_path8, self.opt_moves8 = [1, 7, 7, 5, 7, 9, 4, 0, 2, 10], [0, 1, 8, 6, 2, 9], 5
        self.board9, self.opt_path9, self.opt_moves9 = [8, 1, 5, 6, 5, 8, 3, 9, 4, 1], [0, 8, 4, 9], 3
        
    def test_pdf(self):
        """Test from the pdf"""
        board = [1, 3, 10, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1]
        opt_path = [0, 1, 4, 2, 12]
        opt_moves = 4
        self.assertEqual(solve_puzzle(board), (opt_path, opt_moves))

    def test_oneitem(self):
        """1 item list guaranteed to have optimal sol: ([0], 0)"""
        self.assertEqual(solve_puzzle([1]), ([0], 0))

    def test_unsolveable(self):
        """An unsolveable puzzle"""
        board = [0, 1]
        opt_path = None
        opt_moves = None
        self.assertEqual(solve_puzzle(board), (opt_path, opt_moves) )

    def test_various(self):
        """A few random boards for you"""
        # we only check the moves, not the path, since there may be multiple optimal
        # paths for each board.
        self.assertEqual(solve_puzzle(self.board0)[1], self.opt_moves0)
        self.assertEqual(solve_puzzle(self.board1)[1], self.opt_moves1)
        self.assertEqual(solve_puzzle(self.board2)[1], self.opt_moves2)
        self.assertEqual(solve_puzzle(self.board3)[1], self.opt_moves3)
        self.assertEqual(solve_puzzle(self.board4)[1], self.opt_moves4)
        self.assertEqual(solve_puzzle(self.board5)[1], self.opt_moves5)
        self.assertEqual(solve_puzzle(self.board6)[1], self.opt_moves6)
        self.assertEqual(solve_puzzle(self.board7)[1], self.opt_moves7)
        self.assertEqual(solve_puzzle(self.board8)[1], self.opt_moves8)
        self.assertEqual(solve_puzzle(self.board9)[1], self.opt_moves9)

if __name__ == '__main__':
    unittest.main()
    