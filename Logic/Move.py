from enum import Enum


class Aim(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


def move(pos, aim):
    xPos, yPos = pos

    if aim == Aim.Up:
        return (xPos, yPos - 1)
    elif aim == Aim.Right:
        return (xPos + 1, yPos)
    elif aim == Aim.Down:
        return (xPos, yPos + 1)
    elif aim == Aim.Left:
        return (xPos - 1, yPos)
    else:
        print("Unknown aim encountered.")
        raise ValueError
