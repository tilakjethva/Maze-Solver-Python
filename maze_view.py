import os

import pygame

height = 700
width = 100
pixel = 10
totalColumn = 1
totalRow = 1
maze = []

# define basic colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = game_folder + "/img/"


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        global maze
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 's', 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 'i', 0, 1, 1, 0, 1, 0, 1, 'd', 1, 1], [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, '2', 1, 0, 'e', 1], [1, 0, 0, 1, 1, 0, 1, 0, 'c', 1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 'b', 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 'c', 1], [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 'f', 0, 0, 1, 0, 0, 0, 1, 1, '3', 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 'g', 1, 1, 0, 1, 1], [1, 'a', 0, 1, 0, 0, 0, '4', 0, 0, 0, 'h', 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        global totalColumn
        totalColumn = len(maze[0])

        global totalRow
        totalRow = len(maze)

        global pixel
        pixel = int(height / totalRow)

        global width
        width = pixel * totalRow

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
                candy = Candy(row, column)
                all_sprites.add(candy)
            elif str(maze[row][column]) == "s":
                player = Player(row, column)
                all_sprites.add(player)
            elif str(maze[row][column]) == "a" or str(maze[row][column]) == "d" or str(maze[row][column]) == "f" or str(maze[row][column]) == "h":
                key = Key(row, column, maze[row][column])
                all_sprites.add(key)
            elif str(maze[row][column]) == "b" or str(maze[row][column]) == "i" or str(maze[row][column]) == "g" or str(maze[row][column]) == "c":
                door = Door(row, column, maze[row][column])
                all_sprites.add(door)
            elif maze[row][column] == 1:
                block = screen.blit(block_surf, (column * pixel, row * pixel))
            else:
                ghost = Ghost(row, column)
                all_sprites.add(ghost)
                placex.append(row * pixel)
                placey.append(column * pixel)

            if isRowIncreased == 1:
                row = row + 1
                if row >= totalColumn:
                    row = 0
                    column = column + 1 if column < totalColumn-1 else 0
            else:
                column = column + 1
                if column >= totalRow:
                    column = 0
                    row = row + 1 if row < totalRow-1 else 0


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

# display_surf = None
image_surf = None

# BackGround = Background()
# MaZe = Maze()
all_sprites = pygame.sprite.Group()  # group of sprites

Maze(screen)
all_sprites.draw(screen)
pygame.display.flip()

# main game loop
running = True
while running:
    # #     # keep loop running at the right speed
    # clock.tick(fps)  # speed of the loop
    # #     # events
    # for event in pygame.event.get():
    #     Event1 = pygame.event.Event(1)
    #     # check for closing the window
    #     if event.type == pygame.QUIT:
    #         running = False
    #     elif event.type == Event1:
    #         running = False

    Maze(screen)
    all_sprites.draw(screen)
    pygame.display.flip()  # quicker process to draw things
    # pygame.event.post(Event1)

pygame.quit()
