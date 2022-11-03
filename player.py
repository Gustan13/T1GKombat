from cmath import rect
import pygame
from hitbox import *

pygame.init()

class player:

    def __init__(self, num, color):
        if (num == 0):
            self.rect = pygame.Rect(100,300,100,200)
        else:
            self.rect = pygame.Rect(800,300,100,200)

        self.color = color
        self.default_color = color

        self.hit_timer = 0
        self.hurt_timer = 30

        self.punching = False
        self.canMove = True

        self.type = 0
        self.dir = 0
        self.num = num

        self.hurt = False
        self.life = 100

    def punch(self, hitboxes, type):
        if self.hit_timer == 0:
            hitboxes.append(hitbox(self.num, self.rect.right, type))
        
        self.canMove = False
        if self.hit_timer <= -30:
            self.hit_timer = 0
            self.canMove = True
            self.punching = False

    def timer_update(self):
        self.hit_timer -= 1

    def move(self, x):
        self.rect = self.rect.move(x * 15, 0)

    def keyboard_check(self):
        keys = pygame.key.get_pressed()

        if not self.canMove:
            return
    
        if ((keys[pygame.K_h] and self.num == 0) or (keys[pygame.K_4] and self.num == 1)) and self.hit_timer <= 0:
            self.punching = True
            self.hit_timer = 0
            self.type = 0
            self.canMove = False
        
        elif ((keys[pygame.K_j] and self.num == 0) or (keys[pygame.K_5] and self.num == 1)) and self.hit_timer <= 0:
            self.punching = True
            self.hit_timer = 0
            self.type = 1
            self.canMove = False
        elif ((keys[pygame.K_k] and self.num == 0) or (keys[pygame.K_6] and self.num == 1)) and self.hit_timer <= 0:
            self.punching = True
            self.hit_timer = 0
            self.type = 2
            self.canMove = False
        
        elif (keys[pygame.K_a] and self.num == 0) or (keys[pygame.K_LEFT] and self.num == 1):
            self.dir = -1
        elif (keys[pygame.K_d] and self.num == 0) or (keys[pygame.K_RIGHT] and self.num == 1):
            self.dir = 1
        elif (not keys[pygame.K_d] and not keys[pygame.K_a] and self.num == 0) or (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.num == 1):
            self.dir = 0

    def hit_check(self, hitboxes):

        if self.hurt:
            self.hurt_timer -= 1
            if self.hurt_timer <= 0:
                self.color = self.default_color
                self.canMove = True
                self.hurt_timer = 30
                self.hurt = False
            return

        for i in hitboxes:
            
            if self.rect.colliderect(i.rect):
                self.color = (255,255,255)
                hitboxes.clear()
                self.hurt = True
                self.canMove = False
        

    def update(self, hitboxes):
        self.timer_update()
        self.keyboard_check()
        self.hit_check(hitboxes)

        if self.canMove:
            self.move(self.dir)

        if self.punching:        
            self.punch(hitboxes, self.type)
                
