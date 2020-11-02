import pygame


class MazeGrid:

    def __init__(self, x_cells, y_cells):
        # TODO
        # Generate 2D list of cells
        # Cells have 4 neighbours and optionally share a wall with them
        # Referencing a neighbour should/can automatically reference the correct wall between them
        pass


def drawGrid(screen):
    x, y = screen.get_size()
    mazeSurface = pygame.Surface((int(x * 0.9), int(y * 0.9)))
    mazeSurface.fill((55, 55, 55))
    pygame.draw.rect(mazeSurface, (255, 255, 255), (5, 5, 500, 500), 2)

    return mazeSurface
