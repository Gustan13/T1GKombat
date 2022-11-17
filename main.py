import pygame
import os
import player
import health_bar

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

    player_1 = player.player(0, (100, 0, 0), "binder")
    player_2 = player.player(1, (0, 100, 0), "binder")
    health_bar_1 = health_bar.health_bar(player_1.num)
    health_bar_2 = health_bar.health_bar(player_2.num)

    hitboxes = []

    running = True

    allsprites = pygame.sprite.RenderPlain((player_1))

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_1.update(hitboxes)
        player_2.update(hitboxes)

        health_bar_1.update(player_1.num, player_1)
        health_bar_2.update(player_2.num, player_2)

        for i in hitboxes:
            i.update(hitboxes)

        pygame.draw.rect(screen, player_1.color, player_1.rect)
        pygame.draw.rect(screen, player_2.color, player_2.rect)

        pygame.draw.rect(screen, (255,0,0), (50, 25, 425, 50))
        pygame.draw.rect(screen, (255,0,0), (525, 25, 425, 50))

        pygame.draw.rect(screen, (0,255,0), health_bar_1.rect)
        pygame.draw.rect(screen, (0,255,0), health_bar_2.rect)

        for i in hitboxes:
            pygame.draw.rect(screen, (0,0,255), i.rect)

        allsprites.draw(screen)

        clock.tick(30)
        pygame.display.flip()
        screen.fill((0,0,0))

    pygame.quit()

main()
