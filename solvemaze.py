import sys


# Authors
# Group 22
# Chendursundaran KUMARAGURUBARAN
# Jenoh JOHNSON
# Tilak Chandrakantbhai JETHVA
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f


class AmazeSolver:

    def __init__(self, input_file):
        self.input_file = input_file

        # Read the input_file into grid
        with open(input_file, "r") as f:
            self.maze = []
            for i, line in enumerate(f.readlines()):
                self.maze.append([])
                for j, pos in enumerate(line.split()):
                    if pos == 's':  # start position
                        self.start = (i, j)
                        self.maze[i].append(pos)
                    elif pos == 'e':  # end position
                        self.end = (i, j)
                        self.maze[i].append(pos)
                    else:
                        self.maze[i].append(int(pos))


        print(self.maze)
        print(self.start)
        print(self.end)

    def astar_solve(self):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = Node(None, self.start)
        end_node = Node(None, self.end)

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            open_list.sort()

            # Pop current off open list, add to closed list
            current_node = open_list.pop(0)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path

            adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

            # Loop through children
            for position in adjacent_squares:

                child = self.get_child(current_node, position)

                if child is None:
                    continue

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                            (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

    def get_child(self, current_node, next_position):
        # Get node position
        (x_position, y_position) = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])

        # Make sure within range
        if x_position > (len(self.maze) - 1) or x_position < 0 or y_position > (
                len(self.maze[len(self.maze) - 1]) - 1) or y_position < 0:
            return None

        # Make sure walkable terrain
        if self.maze[x_position][y_position] != 0:
            return None

        node_position = (x_position, y_position)

        # Create new child
        new_child = Node(current_node, node_position)

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
