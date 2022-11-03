import pygame
import os
import player_1
import hitbox


if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sounds disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pygame.init()
screen = pygame.display.set_mode((1000, 600), pygame.SCALED)
pygame.display.set_caption("Mortal Kombat")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

def main():

    player = player_1.player()

    hitboxes = []

    running = True


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(hitboxes)

        for i in hitboxes:
            i.update(hitboxes)

        pygame.draw.rect(screen, (100,0,0), player.rect)

        for i in hitboxes:
            pygame.draw.rect(screen, (0,0,255), i.rect)

        clock.tick(60)
        pygame.display.flip()
        screen.fill((0,0,0))

    pygame.quit()

main()
