# Authors
# Group 22
# Chendursundaran KUMARAGURUBARAN
# Jenoh JOHNSON
# Tilak Chandrakantbhai JETHVA

import sys

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
                    elif pos == '0' or pos == '1': # path and wall
                        self.maze[i].append(int(pos))
                    else:
                        self.maze[i].append(pos)

        self.keys_found = {} # dict of keys and isRetrieved
        self.door_dict = {'g':'f', 'c':'d', 'b':'a', 'h':'i'}

        print(self.maze)
        print(self.start)
        print(self.end)

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
        elm = self.maze[row][col]

        # Save the keys
        if elm in self.door_dict.values() and elm not in self.keys_found:
            self.keys_found[elm] = True
            is_key_node = True
        # Use the key for the door
        elif elm in self.door_dict.keys() and self.door_dict[elm] in self.keys_found:
            pass
        # Make sure its a path
        elif elm not in [0, self.START, self.END]:
            return None

        node_position = (row, col)

        # Create new child
        new_child = Node(current_node, node_position)

        # save the keys
        if is_key_node:
            new_child.key = elm

        return new_child


def main():
    if len(sys.argv) == 1:
        print("Please provide an input maze file as argument!")
    else:
        input_file = sys.argv[1]
    solver = AmazeSolver(input_file)
    path = solver.astar_solve()
    print(path)


if __name__ == "__main__":
    main()
