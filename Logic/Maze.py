import pygame
import random
from Logic.MazeCell import MazeCell
from Logic.MazeCell import Aim
from Logic.MazeWall import MazeWall


class Maze:

    def initBeginEnd(self):
        start = random.randrange(0, len(self.cellList))
        end = random.randrange(0, len(self.cellList))

        self.cellList[start][0].topWall.open()
        self.cellList[end][len(self.cellList[0]) - 1].botWall.open()

    def initWalls(self, cellList):

        for col in cellList:
            for cell in col:
                cell_x, cell_y = cell.pos

                dbg = True if cell_x > 10 else False

                # First/last column
                setRight = True
                if cell_x == 0:
                    cell.addWall(Aim.Left, True)
                elif cell_x == len(cellList) - 1:
                    cell.addWall(Aim.Right, True)
                    setRight = False

                # First/last row
                setBot = True
                if cell_y == 0:
                    cell.addWall(Aim.Top, True)
                elif cell_y == len(col) - 1:
                    cell.addWall(Aim.Bottom, True)
                    setBot = False

                # Only set right/bottom neighbours, should cover all cells
                if setRight:
                    cellList[cell_x + 1][cell_y].leftWall = cell.rightWall
                    cell.addWall(Aim.Right)

                if setBot:
                    cell.addWall(Aim.Bottom)
                    cellList[cell_x][cell_y + 1].topWall = cell.botWall
        return

    def initCells(self, mazeSize):

        cellList = []
        for col_x in range(mazeSize[0]):
            column = []

            for cell_y in range(mazeSize[1]):
                column.append(MazeCell((col_x, cell_y), self.CELL_SIZE))

            cellList.append(column)

        # Seperate initialisation for the shared walls
        self.initWalls(cellList)

        return cellList

    def __init__(self, screen_size):
        """
        Class for making a maze
        """
        self.CELL_SIZE = 24
        self.mazeScreen = pygame.Surface(screen_size)
        self.mazeScreen.fill((200, 200, 200))
        pygame.draw.rect(self.mazeScreen, (10, 10, 10),
                         ((0, 0), (self.mazeScreen.get_size())), 3)

        screenX, screenY = screen_size
        mazeSize = (int(screenX / self.CELL_SIZE),
                    int(screenY / self.CELL_SIZE))
        self.cellList = self.initCells(mazeSize)
        self.initBeginEnd()

        return

    def draw(self):
        for col in self.cellList:
            for cell in col:
                cell.draw(self.mazeScreen)
        return self.mazeScreen
