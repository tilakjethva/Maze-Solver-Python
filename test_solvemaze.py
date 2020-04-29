import unittest

from solvemaze import AmazeSolver


class TestAmazeSolver(unittest.TestCase):

    def test_maze1(self):
        solver = AmazeSolver("input\\Maze1.txt")
        path = solver.astar_solve()
        self.assertEqual(path, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3),
                                (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)],
                         "Should be the maze path")

    def test_maze2(self):
        solver = AmazeSolver("input\\Maze2.txt")
        path = solver.astar_solve()
        self.assertEqual(path,  [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (2, 3), (2, 4),
                                 (2, 5), (1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1),
                                 (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5),
                                 (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)],
                         "Should be the maze path")

    def test_maze3(self):
        solver = AmazeSolver("input\\Maze3.txt")
        path = solver.astar_solve()
        self.assertEqual(path,  [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 1), (7, 1),
                                 (8, 1), (8, 2), (9, 2), (10, 2), (10, 1), (11, 1), (12, 1), (13, 1),
                                 (13, 2), (14, 2), (15, 2), (15, 1), (15, 2), (14, 2), (13, 2), (13, 1),
                                 (12, 1), (11, 1), (10, 1), (10, 2), (9, 2), (8, 2), (8, 3), (7, 3), (7, 4),
                                 (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (7, 8), (8, 8),
                                 (8, 7), (8, 6), (8, 5), (9, 5), (10, 5), (10, 4), (11, 4), (12, 4), (13, 4),
                                 (13, 5), (13, 6), (13, 7), (13, 8), (12, 8), (11, 8), (11, 9), (11, 10),
                                 (11, 11), (10, 11), (9, 11), (9, 12), (9, 13), (10, 13), (10, 14), (11, 14),
                                 (12, 14), (12, 13), (12, 12), (13, 12), (13, 11), (13, 10), (14, 10), (15, 10),
                                 (15, 11), (15, 10), (14, 10), (13, 10), (13, 11), (13, 12), (12, 12), (12, 13),
                                 (12, 14), (11, 14), (10, 14), (10, 13), (9, 13), (9, 12), (9, 11), (10, 11),
                                 (11, 11), (11, 10), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (13, 6),
                                 (13, 5), (13, 4), (12, 4), (11, 4), (10, 4), (10, 5), (9, 5), (8, 5), (7, 5),
                                 (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9),
                                 (1, 10), (1, 11), (1, 12), (2, 12), (2, 13), (2, 14), (1, 14), (1, 15), (1, 16),
                                 (2, 16), (3, 16), (3, 15), (4, 15), (3, 15), (4, 15), (5, 15), (5, 16)],
                         "Should be the maze path")


if __name__ == '__main__':
    unittest.main()