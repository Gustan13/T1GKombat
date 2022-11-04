from cmath import rect
import pygame
from hitbox import *

pygame.init()

class player:

    def __init__(self, num, color):
        if (num == 0):
            self.rect = pygame.Rect(100,300,100,200)

            self.high_punch = pygame.K_h
            self.low_kick = pygame.K_j
            self.heavy_attack = pygame.K_k
            self.left = pygame.K_a
            self.right = pygame.K_d

        else:
            self.rect = pygame.Rect(800,300,100,200)

            self.high_punch = pygame.K_8
            self.low_kick = pygame.K_9
            self.heavy_attack = pygame.K_0
            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT

        self.color = color
        self.default_color = color

        self.hit_timer = 0
        self.hurt_timer = 30
        self.attack_cooldown = 15

        self.punching = False
        self.canMove = True

        self.type = 0
        self.dir = 0
        self.num = num

        self.hurt = False
        self.life = 100
        self.punches_left = 3

    def punch(self, hitboxes, type):
        if self.hit_timer == -10:
            hitboxes.append(hitbox(self.num, self.rect.right, type))
        
        self.canMove = False
        if self.hit_timer <= -20:
            self.hit_timer = 0
            self.canMove = True
            self.punching = False
            self.punches_left -= 1
            self.attack_cooldown = 50

    def timer_update(self):
        self.hit_timer -= 1

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            return

        self.punches_left = 3

    def move(self, x):
        self.rect = self.rect.move(x * 15, 0)

    def keyboard_check(self):
        keys = pygame.key.get_pressed()

        if not self.canMove:
            return
    
        if keys[self.left]:
            self.dir = -1
        elif keys[self.right]:
            self.dir = 1
        elif not keys[self.left] and not keys[self.right]:
            self.dir = 0

        if self.hit_timer > 0 or self.punches_left < 1:
            return

        if keys[self.high_punch]:
            self.punching = True
            self.hit_timer = 0
            self.type = 0
            self.canMove = False
        
        elif keys[self.low_kick]:
            self.punching = True
            self.hit_timer = 0
            self.type = 1
            self.canMove = False

        elif keys[self.heavy_attack]:
            self.punching = True
            self.hit_timer = 0
            self.type = 2
            self.canMove = False

    def hit_check(self, hitboxes):

        for i in hitboxes:
            if self.rect.colliderect(i.rect):
                self.color = (255,255,255)
                hitboxes.clear()

                self.hurt = True
                self.canMove = False
                self.punching = False
                self.hurt_timer = 30

        if not self.hurt:
            return
        
        self.hurt_timer -= 1
        if self.hurt_timer <= 0:
            self.color = self.default_color
            self.canMove = True
            self.hurt = False


    def update(self, hitboxes):
        self.timer_update()
        self.keyboard_check()
        self.hit_check(hitboxes)

        if self.canMove:
            self.move(self.dir)

        if self.punching:        
            self.punch(hitboxes, self.type)
                
