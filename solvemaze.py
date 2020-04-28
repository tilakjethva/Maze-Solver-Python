import sys

# Authors
# Group 22
# Chendursundaran KUMARAGURUBARAN
# Jenoh JOHNSON
# Tilak Chandrakantbhai JETHVA
class AmazeSolver:

    def __init__(self, input_file):
        self.input_file = input_file


def main():
    if len(sys.argv) == 1:
        print("Please provide an input maze file as argument!")
    else:
        input_file = sys.argv[1]
    solver = AmazeSolver(input_file)


if __name__ == "__main__":
    main()