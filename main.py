import pygame
from game import Game

pygame.init()
game = Game(50,30)
while True:
    game.getEvents()
    game.render()