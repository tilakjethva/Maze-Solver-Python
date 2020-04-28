import sys


class MazeSolver:

    def __init__(self, input_file):
        self.input_file = input_file


def main():
    if len(sys.argv) == 1:
        print("Please provide an input maze file as argument!")
    else:
        input_file = sys.argv[1]


if __name__ == "__main__":
    main()