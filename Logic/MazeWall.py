
class MazeWall:
    def __init__(self, isEdge=False) -> None:
        self.isEdge = isEdge
        self.isOpen = False

    def open(self):
        self.isOpen = True

    def close(self):
        self.isOpen = False
