import pygame
import os
import player
import health_bar
import power_bar

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

    power_bar_1 = power_bar.power_bar()
    power_bar_2 = power_bar.power_bar()

    hitboxes = []

    running = True

    allsprites = pygame.sprite.RenderPlain((player_1))

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_2.update(screen, hitboxes)

        for i in hitboxes:
            i.update(screen, hitboxes)

        player_1.update(screen, hitboxes)

        for i in hitboxes:
            i.update(screen, hitboxes)

        health_bar_1.update(screen, player_1.num, player_1)
        health_bar_2.update(screen, player_2.num, player_2)

        power_bar_1.update(screen, player_1.num, player_1)
        power_bar_1.update(screen, player_2.num, player_2)

        allsprites.draw(screen)

        clock.tick(30)
        pygame.display.flip()

        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,0,0), (50, 25, 425, 50))
        pygame.draw.rect(screen, (255,0,0), (525, 25, 425, 50))

    pygame.quit()

main()
