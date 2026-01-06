# Pygame Drawing
# Author: Ubial
# 5 January 2026

import pygame


def game():
    pygame.init()

    WHITE = (240, 255, 240)
    BLACK = (0, 0, 0)
    RED = (240, 0, 0)
    GREEN = (0, 250, 0)
    BLUE = (0, 0, 245)
    GREY = (150, 145, 150)

    WIDTH = 600
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Masterpiece")

    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # draw a red rectangle in the middle of the screen
        pygame.draw.rect(screen, RED, (WIDTH / 4 - 100, HEIGHT / 2 - 30, 300, 90))
        # draw a blue circle on top of the red rectangle
        pygame.draw.circle(screen, BLUE, (WIDTH / 4, HEIGHT / 4 - 80), 40)

        # draw a 6 lines from the top middle to the middle right
        # they repeat moving down the y-axis 10 px each
        for offset in range(5):
            pygame.draw.line(
                screen,
                GREEN,
                (WIDTH / 2 + 20, 20 + offset * 10),
                (WIDTH - 20, HEIGHT / 2 - 20 + offset * 10),
            )

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
