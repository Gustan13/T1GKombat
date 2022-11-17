import pygame
from hitbox import *
from image_loader import *

pygame.init()

class player(pygame.sprite.Sprite):

    def __init__(self, num, color, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name

        if (num == 0):
            self.rect = pygame.Rect(100,300,100,200)

            self.high_punch = pygame.K_h
            self.low_kick = pygame.K_j
            self.heavy_attack = pygame.K_k

            self.up_defense = pygame.K_w
            self.down_defense = pygame.K_s

            self.left = pygame.K_a
            self.right = pygame.K_d

        else:
            self.rect = pygame.Rect(800,300,100,200)

            self.high_punch = pygame.K_8
            self.low_kick = pygame.K_9
            self.heavy_attack = pygame.K_0

            self.up_defense = pygame.K_UP
            self.down_defense = pygame.K_DOWN

            self.left = pygame.K_LEFT
            self.right = pygame.K_RIGHT

        self.color = color
        self.default_color = color

        self.hit_timer = 0
        self.hurt_timer = 30
        self.attack_cooldown = 15

        self.punching = False
        self.canMove = True

        self.defending = -1

        self.attack_number = 0
        self.dir = 0
        self.num = num

        self.hurt = False
        self.life = 100
        self.punches_left = 3
        self.power = 0

        self.animator = image_loader()

        self.current_frame = 0
        self.current_animation = []
        self.current_animation = self.animator.load_images(1, "idle", "binder", self.current_animation)
        self.image = self.current_animation[0]

    def timer_update(self):
        self.hit_timer -= 1

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            return
        self.punches_left = 3

    def start_attack(self, attack_number):
        if attack_number == 2 and self.power < 3:
            return
        elif attack_number == 2 and self.power >= 3:
            self.power -= 3

        self.punching = True
        self.hit_timer = 0
        self.canMove = False

        self.attack_number = attack_number

    def end_attack(self):
        self.punching = False
        self.hit_timer = 10
        self.canMove = True

        self.punches_left -= 1
        self.attack_cooldown = 50

    def punch(self, hitboxes, attack_number):
        if not self.punching:
            return

        if self.hit_timer == -10:
            hitboxes.append(hitbox(self.num, self.rect.right, attack_number))
        
        if self.hit_timer <= -20:
            self.end_attack()

    def move(self, x):
        self.rect = self.rect.move(x * 15, 0)

    def keyboard_check(self):
        keys = pygame.key.get_pressed()

        if not self.canMove:
            return
    
        elif keys[self.up_defense]:
            self.defending = 0
        elif keys[self.down_defense]:
            self.defending = 1
        else:
            self.defending = -1

        if keys[self.left]:
            self.dir = -1
        elif keys[self.right]:
            self.dir = 1
        elif not keys[self.left] and not keys[self.right]:
            self.dir = 0

        if self.hit_timer > 0 or self.punches_left < 1:
            return

        if keys[self.high_punch]:
            self.start_attack(0)
        
        elif keys[self.low_kick]:
            self.start_attack(1)

        elif keys[self.heavy_attack]:
            self.start_attack(2)

    def start_damage(self, attack_number):
        self.color = (255,255,255)
        self.hurt = True
        self.canMove = False
        self.punching = False

        if attack_number != 2:
            self.hurt_timer = 30
            return

        self.hurt_timer = 5

    def end_damage(self, attack_number):
        if (self.hurt_timer == 5 and attack_number == 2) or self.hurt_timer == 30:
            self.life -= 10

        self.hurt_timer -= 1

        if self.hurt_timer <= 0:
            self.color = self.default_color
            self.canMove = True
            self.hurt = False
            self.dir = 0
            return

        if attack_number == 2:
            self.dir = self.num * 2 - 1
            self.move(self.dir * 3)

    def hit_check(self, hitboxes):
        for i in hitboxes:
            if not self.rect.colliderect(i.rect):
                continue

            if self.defending != i.attack_number:
                self.start_damage(i.attack_number)
                self.hej = i.attack_number
                break
            else:
                if self.power < 9:
                    self.power += 1 

        if not self.hurt:
            return
        
        self.end_damage(self.hej)

    def update(self, screen, hitboxes):
        self.timer_update()
        self.keyboard_check()
        self.hit_check(hitboxes)

        self.punch(hitboxes, self.attack_number)

        if self.canMove:
            self.move(self.dir)

        pygame.draw.rect(screen, self.color, self.rect)
                
