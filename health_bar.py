import pygame
from player import *

pygame.init()

class health_bar():

    def __init__(self, num):
        self.rect = pygame.Rect(num * 475 + 50, 25, 425, 25)

    def update(self, screen, num, player):
        self.rect = pygame.Rect(num * 475 + 50 + (425 - player.life * 4.25)*num, 25, player.life * 4.25, 25)
        pygame.draw.rect(screen, (0,255,0), self.rect)