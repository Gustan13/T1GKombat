import pygame

pygame.init()

class hitbox:

    def __init__(self, player, x, type):
        self.timer = 30
        self.num = player

        if player == 0:
            self.side = 0
        else:
            self.side = 1

        if type == 0:
            self.size = 50
            self.y = 300
            self.x = x - player*150
        
        elif type == 1:
            self.size = 50
            self.y = 450
            self.x = x - player*150

        elif type == 2:
            self.size = 200
            self.y = 300
            self.x = x - player*150

        self.rect = pygame.Rect(self.x, self.y, 50, self.size)

    def update(self, hitboxes):
        self.timer -= 1

        if self.timer <= 0:
            hitboxes.remove(self)
            self.timer = 30