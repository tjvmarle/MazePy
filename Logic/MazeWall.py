# from Logic.Maze import Maze
import pygame


class MazeWall:
    WALL_COLOR = (10, 10, 10)
    OPEN_COLOR = (200, 200, 200)

    def __init__(self, startPos, endPos, isEdge=False) -> None:
        self.startPos = startPos
        self.endPos = endPos
        self.isEdge = isEdge
        self.isOpen = False

    def open(self):
        if self.isEdge:
            print("Open edge!!")

        self.isOpen = True
        return True

    def close(self):
        self.isOpen = False

    def draw(self, surface):
        if not self.isEdge:
            pygame.draw.line(
                surface,  MazeWall.OPEN_COLOR if self.isOpen else MazeWall.WALL_COLOR, self.startPos, self.endPos, 2)

        elif self.isEdge and self.isOpen:
            pygame.draw.line(
                surface,  (0, 255, 0), self.startPos, self.endPos, 2)
