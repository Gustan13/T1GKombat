import pygame
import os

pygame.init()

class image_loader():

    def __init__(self):
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]

    def load_images(self, size, character_state, name, frames):

        if size == 0:
            return

        fullname = os.path.join(self.main_dir, "data", name, character_state, character_state + " (" + str(size) + ")" + ".gif")

        self.load_images(size - 1, character_state, name, frames)
        frames.append(pygame.image.load(fullname))

        return frames