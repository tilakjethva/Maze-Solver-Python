import os
import sys
import time

import pygame

from solvemaze import AmazeSolver

height = 700
pixel = 10
FPS = 10
player = ""
candy = ""

# define basic colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = game_folder + "/img/"


def solve_maze():
    # solve the maze
    input_file = ""
    if len(sys.argv) == 1:
        print("Please provide an input maze file as argument!")
        quit()
    else:
        input_file = sys.argv[1]
    solver = AmazeSolver(input_file)
    mazepath = solver.astar_solve()
    return solver.get_maze_grid(), mazepath


class Maze(pygame.sprite.Sprite):
    def __init__(self, maze):

        totalColumn = len(maze[0])

        totalRow = len(maze)

        global pixel
        pixel = int(height / totalRow)

        width = pixel * totalColumn

        self.screen = pygame.display.set_mode((width, height))

        placex = []
        placey = []

        isRowIncreased = 1 if totalRow > totalColumn else 0

        row = 0
        column = 0
        for i in range(0, totalColumn * totalRow):
            if maze[row][column] == 0:
                all_sprites.add(Draw(row, column, "path"))
            elif str(maze[row][column]) == "e" or str(maze[row][column]) == "s":
                all_sprites.add(Draw(row, column, str(maze[row][column])))
            elif str(maze[row][column]) == "a" or str(maze[row][column]) == "d" or str(maze[row][column]) == "f" or str(
                    maze[row][column]) == "h" or str(maze[row][column]) == "b" or str(maze[row][column]) == "i" or str(maze[row][column]) == "g" or str(
                    maze[row][column]) == "c":
                all_sprites.add(Draw(row, column, maze[row][column]))
            elif maze[row][column] == -1:
                all_sprites.add(Draw(row, column, "ghost_path"))
            elif maze[row][column] == 1:
                block_surf = pygame.transform.scale(
                    (pygame.image.load(os.path.join(img_folder, "block.png")).convert()),
                    (pixel, pixel))
                block = self.screen.blit(block_surf, (column * pixel, row * pixel))
            else:
                all_sprites.add(Draw(row, column, "ghost"))
                placex.append(row * pixel)
                placey.append(column * pixel)

            if isRowIncreased == 1:
                row = row + 1
                if row >= totalRow:
                    row = 0
                    column = column + 1 if column < totalColumn - 1 else 0
            else:
                column = column + 1
                if column >= totalColumn:
                    column = 0
                    row = row + 1 if row < totalRow - 1 else 0

    def get_screen(self):
        return self.screen


class Draw(pygame.sprite.Sprite):
    def __init__(self, row, column, identifier):
        pygame.sprite.Sprite.__init__(self)  # for sprite working

        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, identifier+".png")).convert()),
                                            (pixel, pixel))
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


# initialize pygame and create window
pygame.init()  # start pygame

solver = solve_maze()
mazepath = solver[1]

all_sprites = pygame.sprite.Group()
maze = Maze(solver[0])
screen = maze.get_screen()

pygame.display.set_caption("Maze Solver Group 22")  # name of my window
clock = pygame.time.Clock()

all_sprites.draw(screen)

count = 0
# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)

    pos = mazepath[count]
    x, y = pos

    if pos != mazepath[len(mazepath) - 1]:
        all_sprites.add(Draw(x, y, "path"))

    all_sprites.remove(player)
    player = Draw(x, y, "s")
    all_sprites.add(player)
    pygame.display.update()
    all_sprites.draw(screen)
    time.sleep(.05)

    if pos == mazepath[len(mazepath) - 1]:
        all_sprites.remove(candy)
        pygame.display.update()
        all_sprites.draw(screen)
        running = False

    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

    count += 1
