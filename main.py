# Ulam spiral 2023
# By Tomasz Golaszewski
# 01.2023

# Quick project to draw Ulam spiral

import pygame
import random
import math

# global settings
WIN_WIDTH, WIN_HEIGHT = 700, 700
FRAMERATE = 25
STEP_SIZE = 35
FONT_SIZE = 30
MAX_N = 100

WHITE = (255, 255, 255)

def is_prime(x):
# checks if x is prime - return True, or is not - return False
    if x == 1: return False
    i = 2
    sqrt_x = math.sqrt(x)
    while i <= sqrt_x:
        if x % i == 0: return False
        i += 1
    return True

def draw_ulam_spiral(win, win_width, win_height, step_size, draw_line=True, draw_dots=True, draw_numbers=True, font_size=10):
# draw ulam spiral

    # set up spiral
    cols = win_width // step_size - 1
    rows = win_height // step_size - 1
    total_steps = cols * rows
    x = win_width // 2
    y = win_height // 2
    last_x = x
    last_y = y
    current_n = 1
    direction = 0
    turn_counter = 0
    steps_in_line = 1

    if draw_numbers:
        # initialization of font
        font = pygame.font.SysFont('arial', font_size)

    while current_n <= total_steps: # MAX_N:
        if draw_line:
            # draw line
            pygame.draw.line(win, WHITE, (last_x, last_y), (x, y), 1)

        # mark only prime numbers
        if is_prime(current_n):
            if draw_numbers:
                # draw number
                text = font.render(str(current_n), True, WHITE)
                win.blit(text, (x, y))
            if draw_dots:
                # draw dot
                pygame.draw.circle(win, WHITE, (x, y), 3, 0)

        # save the current coordinates to the previous ones
        last_x = x
        last_y = y

        # move according to direction
        if direction == 0:
            x += step_size
        elif direction == 1:
            y -= step_size
        elif direction == 2:
            x -= step_size
        elif direction == 3:
            y += step_size

        # change direction
        if current_n % steps_in_line == 0:
            direction += 1
            if direction == 4: direction = 0
            turn_counter += 1
            if turn_counter % 2:
                steps_in_line += 1

        # next number
        current_n += 1

def run():
# main function - runs the game

# initialize the pygame
    pygame.init()
    pygame.display.set_caption("Ulam Spiral")

    WIN = pygame.display.set_mode((WIN_WIDTH+10, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()
    CURRENT_FRAME = 0

    # draw ulam spiral
    # draw_ulam_spiral(WIN, WIN_WIDTH, WIN_HEIGHT, STEP_SIZE, draw_line=False, draw_dots=True, draw_numbers=False)
    draw_ulam_spiral(WIN, WIN_WIDTH, WIN_HEIGHT, STEP_SIZE, draw_line=True, draw_dots=True, draw_numbers=True, font_size=FONT_SIZE)

    # flip the screen
    pygame.display.update() 

    # main loop
    running = True
    while running:
        CLOCK.tick(FRAMERATE)
        CURRENT_FRAME += 1
        if CURRENT_FRAME == FRAMERATE:
            CURRENT_FRAME = 0
            # print infos about fps and time
            print("FPS: %.2f" % CLOCK.get_fps(), end="\t")
            print("TIME: " + str(pygame.time.get_ticks() // 1000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            # keys that can be pressed only ones
            if event.type == pygame.KEYDOWN:
                # manual close
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    running = False
                    pygame.quit()
                    quit()


if __name__ == "__main__":
    run()

