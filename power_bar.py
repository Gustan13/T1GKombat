import pygame

pygame.init()

class power_bar():

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)

    def update(self, screen, num, player):

        if player.power >= 3:
            pygame.draw.rect(screen, (0,0,255), pygame.Rect(num * 890 + 50, 90, 10, 10))
        
        if player.power >= 6:
            pygame.draw.rect(screen, (0,0,255), pygame.Rect(num * 890 + 50 + 15 + (-num) * 30, 90, 10, 10))

        if player.power == 9:
            pygame.draw.rect(screen, (0,0,255), pygame.Rect(num * 890 + 50 + 30 + (-num) * 60, 90, 10, 10))