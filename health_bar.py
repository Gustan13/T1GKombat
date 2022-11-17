import pygame
from player import *

pygame.init()

class health_bar():

    def __init__(self, num):
        self.rect = pygame.Rect(num * 475 + 50, 25, 425, 50)

    def update(self, num, player):
        self.rect = pygame.Rect(num * 475 + 50 + (425 - player.life * 4.25)*num, 25, player.life * 4.25, 50)