import pygame
from game import Game

pygame.init()
#The first argument handles the number of cells, while the second handles the frame rate. Lowering the framerate increases performance(?
game = Game(50,30)
while True:
    game.getEvents()
    game.render()
