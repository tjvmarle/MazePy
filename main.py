import pygame
import time

from pygame import init
from Logic.MainScreen import MainScreen

# TODO
# Create maze edge
# Create entrance/exit
# Start working on generator

loopGo = True
mainScreen = MainScreen((1280, 720))

while loopGo:

    mainScreen.Tick()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopGo = False
