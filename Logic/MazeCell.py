from enum import Enum


class Direction(Enum):
    Top = 1
    Right = 2
    Bottom = 3
    Left = 4


class MazeCell:
    # TODO: Implement cellwalls, allow to reference walls or neighboring cells.
    # CellWall - Bool is probably enough: True = Closed, False = Open

    def __init__(self) -> None:

        pass
