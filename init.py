import pygame


def initPygame():
    pygame.init()
    pygame.display.set_caption("A maze ing")

    screen_x = 1280
    screen_y = 720
    screen = pygame.display.set_mode((screen_x, screen_y))
    screen.fill((55, 55, 55))
    pygame.display.update()
    return screen
