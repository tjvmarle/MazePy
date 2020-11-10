from enum import Enum

import pygame


class Direction(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3


class MazeCell:
    WALL_COLOR = (10, 10, 10)

    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.abspos = (pos[0] * size, pos[1] * size)
        self.size = size
        self.tWall = None
        self.rWall = None
        self.bWall = None
        self.lWall = None
        return

    def draw(self, surface):
        # TODO:
        # For each wall:
        # Only draw right/bottom, only if not edge

        # Quick drawtest with zigzags
        pos_x, pos_y = self.pos
        if ((pos_x + pos_y) + pos_y % 2) % 2 == 0:
            pygame.draw.line(surface,  MazeCell.WALL_COLOR, self.abspos,
                             (self.abspos[0] + self.size, self.abspos[1] + self.size), 2)
        else:
            pygame.draw.line(surface,  MazeCell.WALL_COLOR, (self.abspos[0], self.abspos[1] + self.size),
                             (self.abspos[0] + self.size, self.abspos[1]), 2)
        return
