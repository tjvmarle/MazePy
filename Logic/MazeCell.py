from enum import Enum
from Logic.MazeWall import MazeWall


class Aim(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3


class MazeCell:
    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.abspos = (pos[0] * size, pos[1] * size)
        self.size = size
        self.topWall = None
        self.rightWall = None
        self.botWall = None
        self.leftWall = None

    def addWall(self, aim, isEdge=False):
        # TODO Finetune the offset a bit --> currently generates 1 empty pixel between cells
        x, y = self.abspos
        xx = x + self.size - 2
        yy = y + self.size - 2

        if aim == Aim.Top:
            self.topWall = MazeWall((x, y), (xx, y), isEdge)
        elif aim == Aim.Right:
            self.rightWall = MazeWall((xx, y), (xx, yy), isEdge)
        elif aim == Aim.Bottom:
            self.botWall = MazeWall((x, yy), (xx, yy), isEdge)
        else:
            self.leftWall = MazeWall((x, y), (x, yy), isEdge)

    def draw(self, surface):
        # Only draw right/bottom, only if not edge
        if self.rightWall is not None:
            self.rightWall.draw(surface)

        if self.botWall is not None:
            self.botWall.draw(surface)

        # Entry point
        if self.topWall is not None and self.topWall.isEdge and self.topWall.isOpen:
            self.topWall.draw(surface)
