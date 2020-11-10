import pygame
import time

from pygame import init
import Visuals.Grid
from Logic.MainScreen import MainScreen

# TODO
# Construct grid / grid logic for given x / y
# Create visuals for cells and open walls
# Clean up the quick-and-dirty first setup
# w: 48, h: 27
#
#
#

loopGo = True
mainScreen = MainScreen((1280, 720))

while loopGo:

    mainScreen.Tick()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopGo = False
