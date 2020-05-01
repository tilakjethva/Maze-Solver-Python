# Authors
# Group 22
# Chendursundaran KUMARAGURUBARAN
# Jenoh JOHNSON
# Tilak Chandrakantbhai JETHVA

import sys
from pprint import pprint

from queue import PriorityQueue


class Node:
    """A node class for Maze"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.key = None

        self.g = 0
        self.h = 0
        self.f = 0

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # hash
    def __hash__(self):
        return hash(self.position)

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f


class AmazeSolver:
    """ You have to solve a maze.
        You start from a fixed position in the maze.
        You need to nd the fastest way to reach the fixed end point.
    """

    START = 's'
    END = 'e'

    def __init__(self, input_file):
        self.input_file = input_file
        self.ghost_positions = []

        # Read the input_file into grid
        with open(input_file, "r") as f:
            self.maze = []
            for i, line in enumerate(f.readlines()):
                self.maze.append([])
                for j, pos in enumerate(line.split()):
                    if pos == self.START:  # start position
                        self.start = (i, j)
                        self.maze[i].append(pos)
                    elif pos == self.END:  # end position
                        self.end = (i, j)
                        self.maze[i].append(pos)
                    elif pos == '0' or pos == '1':  # path and wall
                        self.maze[i].append(int(pos))
                    elif pos.isdigit() and int(pos) >= 2:  # ghosts
                        self.ghost_positions.append((i, j))
                        self.maze[i].append(int(pos))
                    else:
                        self.maze[i].append(pos)

        self.keys_found = {}  # dict of keys and isRetrieved
        self.door_dict = {'g': 'f', 'c': 'd', 'b': 'a', 'i': 'h'}

        self.setup_ghosts()

    def get_maze_grid(self):
        return self.maze

    def setup_ghosts(self):
        """set the cell in the ghosts range to -1"""

        neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for ghost_pos in self.ghost_positions:
            g_range = self.maze[ghost_pos[0]][ghost_pos[1]] -1
            #find the outer range of ghost
            outer_range = [(pos[0] * g_range, pos[1] * g_range) for pos in neighbours]

            for range in outer_range:
                (row, col) = (ghost_pos[0] + range[0], ghost_pos[1] + range[1])

                #find the line of sight
                cells_in_range = self.line_of_sight(ghost_pos[0], ghost_pos[1], row, col)

                for cell in cells_in_range:
                    # Make sure its within range
                    if row > (len(self.maze) - 1) or row < 0 or col > (
                        len(self.maze[len(self.maze) - 1]) - 1) or col < 0:
                        break
                    if self.maze[cell[0]][cell[1]] == 1:
                        break

                    if self.maze[cell[0]][cell[1]] == 0:
                        self.maze[cell[0]][cell[1]] = -1

                    #Fix for corner squares in line of sight
                    if cell[0] != ghost_pos[0] and cell[1] != ghost_pos[1] and self.maze[cell[0]][cell[1]] == -1:
                        if cell[0] - ghost_pos[0] > 0:
                            dy = -1
                        else:
                            dy = 1

                        if cell[1] - ghost_pos[1] > 0:
                            dx = -1
                        else:
                            dx = 1

                        if self.maze[cell[0]+ dy][cell[1]] == 1 and self.maze[cell[0]][cell[1]+ dx] == 1:
                            self.maze[cell[0]][cell[1]] = 0

    def line_of_sight(self, y1, x1, y2, x2):
        """Returns a list of tuples as a line of sight from (y1,x1) to (y2,x2)"""
        swap = 0
        positions = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1

        if x1 < x2:
            sx = 1
        else:
            sx = -1

        if y1 < y2:
            sy = 1
        else:
            sy = -1

        if dy > dx:
            swap = 1
            x,y = y,x
            dx,dy = dy,dx
            sx,sy = sy,sx

        slope = (2 * dy) - dx

        for i in range(0, dx):

            if swap:
                positions.append((x,y))
            else:
                positions.append((y,x))

            while slope >= 0:
                y += sy
                slope = slope - 2*dx

            slope = slope + 2*dy
            x += sx

        positions.append((y2,x2))
        return positions


    def astar_solve(self):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = Node(None, self.start)
        end_node = Node(None, self.end)

        # Initialize both open and closed list
        open_queue = PriorityQueue()
        closed_list = []

        # Add the start node
        open_queue.put(start_node, 0)

        fullpath = []

        # Loop until you find the end
        while not open_queue.empty():

            # Pop current off open list, add to closed list
            current_node = open_queue.get()
            closed_list.append(current_node)

            # Found the end
            if current_node == end_node:
                fullpath += self.build_path(current_node)
                return fullpath

            # Found the key and its not retrieved
            if current_node.key is not None and self.keys_found[current_node.key]:
                self.keys_found[current_node.key] = False
                fullpath += self.build_path(current_node)

                # Clear the lists and add the next node to visit in the queue
                next_node = current_node.parent
                next_node.parent = None
                with open_queue.mutex:
                    open_queue.queue.clear()
                open_queue.put(next_node, 0)
                closed_list.clear()

            adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            # Loop through children
            for position in adjacent_squares:

                child = self.get_child(current_node, position)

                if child is None:
                    continue

                # Child is on the closed list
                if child in closed_list:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = max(abs(child.position[0] - end_node.position[0]),
                              abs(child.position[1] - end_node.position[1]))
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_queue.queue:
                    if child == open_node and child.f > open_node.f:
                        continue

                # Add the child to the open list
                open_queue.put(child, child.f)

    def build_path(self, current_node):
        path = []
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]  # return the  reversed path

    def get_child(self, current_node, next_position):
        # Get node position
        (row, col) = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])

        # Make sure its within range
        if row > (len(self.maze) - 1) or row < 0 or col > (
                len(self.maze[len(self.maze) - 1]) - 1) or col < 0:
            return None

        is_key_node = False
        cell = self.maze[row][col]

        # Save the keys
        if cell in self.door_dict.values() and cell not in self.keys_found:
            self.keys_found[cell] = True
            is_key_node = True
        # Use the key for the door
        elif cell in self.door_dict.keys() and self.door_dict[cell] in self.keys_found:
            pass
        # Make sure its a path
        elif cell not in [0, self.START, self.END]:
            return None

        node_position = (row, col)

        # Create new child
        new_child = Node(current_node, node_position)

        # save the keys
        if is_key_node:
            new_child.key = cell

        return new_child


def main():
    if len(sys.argv) == 1:
        print("Please provide an input maze file as argument!")
        return
    else:
        input_file = sys.argv[1]
    solver = AmazeSolver(input_file)
    path = solver.astar_solve()
    print(path)


if __name__ == "__main__":
    main()
