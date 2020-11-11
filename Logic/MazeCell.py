import pygame
from enum import Enum


class Direction(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3


class MazeCell:
    WALL_COLOR = (10, 10, 10)
    OPEN_COLOR = (200, 200, 200)

    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.abspos = (pos[0] * size, pos[1] * size)
        self.size = size
        self.topWall = None
        self.rightWall = None
        self.botWall = None
        self.leftWall = None
        return

    def draw(self, surface):
        # Only draw right/bottom, only if not edge
        if self.rightWall is not None and not self.rightWall.isEdge and not self.rightWall.isOpen:
            pygame.draw.line(surface,  MazeCell.OPEN_COLOR if self.rightWall.isOpen else MazeCell.WALL_COLOR, (
                self.abspos[0] + self.size, self.abspos[1]), (self.abspos[0] + self.size, self.abspos[1] + self.size), 2)

        if self.botWall is not None and not self.botWall.isEdge and not self.botWall.isOpen:
            pygame.draw.line(surface,  MazeCell.OPEN_COLOR if self.botWall.isOpen else MazeCell.WALL_COLOR, (
                self.abspos[0], self.abspos[1] + self.size), (self.abspos[0] + self.size, self.abspos[1] + self.size), 2)
        return
