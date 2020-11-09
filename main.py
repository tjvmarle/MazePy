import pygame
import time
import Visuals.Grid
from Logic.MainScreen import MainScreen

# TODO
# Construct grid / grid logic for given x / y
# Create visuals for cells and open walls
# Clean up the quick-and-dirty first setup
#
#
#
#

loopGo = True
mainScreen = MainScreen((1280, 720))

while loopGo:

    loopGo = mainScreen.Tick()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopGo = False

    # screen = init.initPygame()
    # x, y = screen.get_size()
    # grid = Visuals.grid.drawGrid(screen)

    # screen.blit(grid, (int(x * 0.05), int(y * 0.05)))
    # pygame.display.update()

    # time.sleep(1.5)
    # loopGo = False
