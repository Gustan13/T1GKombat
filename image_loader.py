import pygame
import os

pygame.init()

class image_loader():

    def __init__(self):
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]

    def load_images(self, size, attack_number, name, frames):

        if size == 0:
            return

        fullname = os.path.join(self.main_dir, "data", name, attack_number, attack_number + " (" + str(size) + ")" + ".gif")

        self.load_images(size - 1, attack_number, name, frames)
        frames.append(pygame.image.load(fullname))

        return frames