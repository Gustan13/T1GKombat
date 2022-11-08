import pygame

pygame.init()

class hitbox:

    def __init__(self, player, x, type):
        self.timer = 5
        self.num = player
        self.type = type

        self.side = 1

        if player == 0:
            self.side = 0

        if type == 0:
            self.set_type(50, x, 300, player)

        elif type == 1:
            self.set_type(50, x, 450, player)

        elif type == 2:
            self.set_type(200, x, 300, player)

        self.rect = pygame.Rect(self.x, self.y, 50, self.size)

    def set_type(self, size, x, y, player):
        self.size = size
        self.y = y
        self.x = x - player*150

    def update(self, hitboxes):
        self.timer -= 1

        if self.timer <= 0:
            hitboxes.remove(self)
            self.timer = 5