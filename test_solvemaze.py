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

if __name__ == '__main__':
    unittest.main()