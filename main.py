import pygame
import os
import player

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sounds disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pygame.init()
screen = pygame.display.set_mode((1000, 600), pygame.SCALED)
pygame.display.set_caption("T1GKombat")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

def main():

    player_1 = player.player(0, (100, 0, 0))
    player_2 = player.player(1, (0, 100, 0))

    hitboxes = []

    running = True


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_1.update(hitboxes)
        player_2.update(hitboxes)

        for i in hitboxes:
            i.update(hitboxes)

        pygame.draw.rect(screen, player_1.color, player_1.rect)
        pygame.draw.rect(screen, player_2.color, player_2.rect)

        for i in hitboxes:
            pygame.draw.rect(screen, (0,0,255), i.rect)

        clock.tick(30)
        pygame.display.flip()
        screen.fill((0,0,0))

    pygame.quit()

main()
