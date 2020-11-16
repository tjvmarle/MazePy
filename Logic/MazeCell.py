from Logic.MazeWall import MazeWall
from Logic.Move import Aim


class MazeCell:
    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.abspos = (pos[0] * size, pos[1] * size)
        self.size = size
        self.walls = {Aim.Up: None, Aim.Right: None,
                      Aim.Down: None, Aim.Left: None}

    def addWall(self, aim, isEdge=False):
        # TODO Finetune the offset a bit --> currently generates 1 empty pixel in cell corners
        x, y = self.abspos
        xx = x + self.size - 2
        yy = y + self.size - 2

        if aim == Aim.Up:
            self.walls[aim] = MazeWall((x, y), (xx, y), isEdge)
        elif aim == Aim.Right:
            self.walls[aim] = MazeWall((xx, y), (xx, yy), isEdge)
        elif aim == Aim.Down:
            self.walls[aim] = MazeWall((x, yy), (xx, yy), isEdge)
        else:
            self.walls[aim] = MazeWall((x, y), (x, yy), isEdge)

    def open(self, aim):
        if self.walls[aim] is not None:
            return self.walls[aim].open()
        return False

    def draw(self, surface):
        # Only draw right/bottom, only if not edge
        if self.walls[Aim.Right] is not None:
            self.walls[Aim.Right].draw(surface)

        if self.walls[Aim.Down] is not None:
            self.walls[Aim.Down].draw(surface)

        # Entry point
        top = self.walls[Aim.Up]
        if top is not None and top.isEdge and top.isOpen:
            top.draw(surface)
