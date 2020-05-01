import os
import sys
import time

import pygame

from solvemaze import AmazeSolver

height = 700
width = 100
pixel = 10
totalColumn = 1
totalRow = 1
maze = []
FPS = 30
player = ""
candy = ""

# define basic colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = game_folder + "/img/"

# solve the maze
input_file = ""
if len(sys.argv) == 1:
    print("Please provide an input maze file as argument!")
    quit()
else:
    input_file = sys.argv[1]

solver = AmazeSolver(input_file)
mazepath = solver.astar_solve()

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        global maze
        maze = solver.get_maze_grid()

        global totalColumn
        totalColumn = len(maze[0])

        global totalRow
        totalRow = len(maze)

        global pixel
        pixel = int(height / totalRow)

        global width
        width = pixel * totalColumn

        # self.image = pygame.Surface([width, height])
        # self.image = pygame.image.load(img_folder + "background.png")
        # self.image.fill(white)
        # self.rect = self.image.get_rect()
        # self.rect.left = 0
        # self.rect.top = 0


class Maze(pygame.sprite.Sprite):
    def __init__(self, screen):

        block_surf = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "block.png")).convert()),
                                            (pixel, pixel))
        placex = []
        placey = []

        isRowIncreased = 1 if totalRow > totalColumn else 0

        row = 0
        column = 0
        for i in range(0, totalColumn * totalRow):
            # print((row, column))
            if maze[row][column] == 0:
                path = Path(row, column)
                all_sprites.add(path)
            elif str(maze[row][column]) == "e":
                global candy
                candy = Candy(row, column)
                all_sprites.add(candy)
            elif str(maze[row][column]) == "s":
                global player
                player = Player(row, column)
                all_sprites.add(player)
            elif str(maze[row][column]) == "a" or str(maze[row][column]) == "d" or str(maze[row][column]) == "f" or str(maze[row][column]) == "h":
                key = Key(row, column, maze[row][column])
                all_sprites.add(key)
            elif str(maze[row][column]) == "b" or str(maze[row][column]) == "i" or str(maze[row][column]) == "g" or str(maze[row][column]) == "c":
                door = Door(row, column, maze[row][column])
                all_sprites.add(door)
            elif maze[row][column] == -1:
                paths = GhostPath(row, column)
                all_sprites.add(paths)
            elif maze[row][column] == 1:
                block = screen.blit(block_surf, (column * pixel, row * pixel))
            else:
                ghost = Ghost(row, column)
                all_sprites.add(ghost)
                placex.append(row * pixel)
                placey.append(column * pixel)

            if isRowIncreased == 1:
                row = row + 1
                if row >= totalRow:
                    row = 0
                    column = column + 1 if column < totalColumn-1 else 0
            else:
                column = column + 1
                if column >= totalColumn:
                    column = 0
                    row = row + 1 if row < totalRow-1 else 0

        # ghost_paths = [(4, 12), (4, 15), (5, 13), (5, 15), (6, 14), (6, 15), (8, 14), (8, 15), (9, 15), (10, 15)]
        # for i in ghost_paths:
        #     x, y = i
        #     g_path = GhostPath(y, x)
        #     all_sprites.add(g_path)


class Path(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "path.png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class Ghost(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "ghost.png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class GhostPath(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "pink_cell.png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class Candy(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "reward.png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class Key(pygame.sprite.Sprite):
    def __init__(self, row, column, alpha):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, alpha+".png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class Door(pygame.sprite.Sprite):
    def __init__(self, row, column, alpha):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, alpha+".png")).convert()),
                                            (pixel, pixel))
        # self.image = pygame.image.load(os.path.join(img_folder, "reward.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = pixel * row
        self.rect.left = pixel * column


class Player(pygame.sprite.Sprite):
    def __init__(self, row, column):  # sprite for a player
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        # self.image = pygame.image.load(os.path.join(img_folder, "pacman.png")).convert()  # look of the sprite
        self.image = pygame.transform.scale((pygame.image.load(os.path.join(img_folder, "pacman.png")).convert()),
                                            (pixel, pixel))
        self.image.set_colorkey(white)  # to delete black things around rect img
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = row * pixel
        self.rect.left = column * pixel


# initialize pygame and create window
pygame.init()  # start pygame

BackGround = Background()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Solver Group 22")  # name of my window
clock = pygame.time.Clock()

# pygame.mixer_music.load("music.mp3")
# pygame.mixer_music.set_volume(0.5)
# pygame.mixer_music.play(-1)


# display_surf = None
image_surf = None

all_sprites = pygame.sprite.Group()

Maze(screen)
all_sprites.draw(screen)
pygame.display.flip()

all_sprites.remove(player)
pygame.display.update()
all_sprites.draw(screen)

def run_player():
    global player
    for i in mazepath:
        x, y = i

        if i != mazepath[len(mazepath) - 1]:
            path = Path(x, y)
            all_sprites.add(path)
            pygame.display.update()
            all_sprites.draw(screen)

        all_sprites.remove(player)
        # print(i)
        player = Player(x, y)
        # path = Path(x, y)
        all_sprites.add(player)
        pygame.display.update()
        all_sprites.draw(screen)
        time.sleep(.1)

        if i == mazepath[len(mazepath) - 1]:
            all_sprites.remove(candy)
            pygame.display.update()
            all_sprites.draw(screen)
            pygame.mixer_music.stop()
            pygame.event.post(pygame.quit())


# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

        run_player()
