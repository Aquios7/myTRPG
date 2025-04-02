'''
Import the required libraries
'''
import pygame
import random


'''
Initialize pygame
'''
pygame.init()

'''
Define the game constants
'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = WHITE

'''
Create the game window
'''
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turn-Based Strategy Game")

'''
Import text window script
'''
import spriteTestModular as tWindow

'''
Define the Player class
'''
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20
        self.selected = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.selected:
            pygame.draw.circle(screen, RED, (self.x, self.y), self.radius, 2)
            tWindow.draw_text_window(screen, 42, SCREEN_HEIGHT - 200, 15, 4, window_type=0,
                                     text="You have chosen {}.".format(self.color))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

'''
Define the Game class
'''
class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def select_player(self, x, y):
        for player in self.players:
            dist = ((player.x - x) ** 2 + (player.y - y) ** 2) ** 0.5
            if dist <= player.radius:
                player.selected = True
            else:
                player.selected = False

    def move_selected_player(self, dx, dy):
        for player in self.players:
            if player.selected:
                player.move(dx, dy)

    def draw(self):
        screen.fill(WHITE)
        for player in self.players:
            player.draw()
        pygame.display.flip()

'''
Create an instance of the Game class
'''
game = Game()

'''
Add players to the game
'''
player1 = Player(100, 100, BLUE)
player2 = Player(200, 200, RED)
game.add_player(player1)
game.add_player(player2)

'''
Game loop
'''
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.select_player(*event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_selected_player(-10, 0)
            elif event.key == pygame.K_RIGHT:
                game.move_selected_player(10, 0)
            elif event.key == pygame.K_UP:
                game.move_selected_player(0, -10)
            elif event.key == pygame.K_DOWN:
                game.move_selected_player(0, 10)

    game.draw()

'''
Quit the game
'''
pygame.quit()