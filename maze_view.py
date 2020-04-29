import pygame
import os

from pygame.sprite import spritecollideany

width = 200
height = 200

# define basic colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = game_folder + "/img/"


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        # self.image = pygame.image.load(img_folder + "background.png")
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0


class Maze(pygame.sprite.Sprite):
    def __init__(self):
        self.W = 10
        self.H = 10
        self.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 's', 1, 0, 1, 0, 1, 0, 0, 1],
                     [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1, 0, 1, 'e', 0, 1],
                     [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def draw(self, screen):
        block_surf = pygame.image.load(os.path.join(img_folder, "block.png")).convert()
        placex = []
        placey = []
        x = 0
        y = 0
        for i in range(0, self.W * self.H):
            if str(self.maze[x][y]) == "s":
                candy = Candy(x, y)
                all_sprites.add(candy)
            elif str(self.maze[x][y]) == "e":
                player = Player()
                all_sprites.add(player)
            elif self.maze[x][y] == 1:
                block = screen.blit(block_surf, (y * 20, x * 20))
            else:
                placex.append(x * 20)
                placey.append(y * 20)

            y = y + 1
            if y > self.H - 1:
                y = 0
                x = x + 1


class Candy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.image.load(os.path.join(img_folder, "cherry.png")).convert()  # look of the sprite
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = 20 * y
        self.rect.left = 20 * x


class Player(pygame.sprite.Sprite):
    def __init__(self):  # sprite for a player
        pygame.sprite.Sprite.__init__(self)  # for sprite working
        self.image = pygame.image.load(os.path.join(img_folder, "pacman.png")).convert()  # look of the sprite
        self.image.set_colorkey(white)  # to delete black things around rect img
        self.rect = self.image.get_rect()  # kind of border around it
        self.rect.top = 20
        self.rect.left = 20


# initialize pygame and create window
pygame.init()  # start pygame

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Solver")  # name of my window
clock = pygame.time.Clock()

# display_surf = None
image_surf = None

BackGround = Background()
MaZe = Maze()
all_sprites = pygame.sprite.Group()  # group of sprites

MaZe.draw(screen)
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

    MaZe.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()  # quicker process to draw things
    # pygame.event.post(Event1)


pygame.quit()
