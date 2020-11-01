import pygame
import init
import time
import Visuals.grid

# TODO
# Construct grid / grid logic for given x / y
# Create visuals for cells and open walls
# Clean up the quick-and-dirty first setup
#
#
#
#

screen = init.initPygame()
x, y = screen.get_size()
grid = Visuals.grid.drawGrid(screen)

screen.blit(grid, (int(x * 0.05), int(y * 0.05)))
pygame.display.update()

time.sleep(1.5)
