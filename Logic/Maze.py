from Logic.MazeCell import MazeCell
import pygame
from Logic.MazeWall import MazeWall


class Maze:

    def initWalls(self, cellList):

        for col in cellList:
            for cell in col:
                cell_x, cell_y = cell.pos

                # First/last column
                setRight = True
                setBot = True
                if cell_x == 0:
                    cell.lWall = MazeWall(True)
                elif cell_x == len(cellList) - 1:
                    cell.rWall = MazeWall(True)
                    setRight = False

                # First/last row
                if cell_y == 0:
                    cell.tWall = MazeWall(True)
                elif cell_y == len(col) - 1:
                    cell.bWall = MazeWall(True)
                    setBot = False

                # Only set right/bottom neighbours, should cover all cells
                if setRight:
                    sharedVertWall = MazeWall()
                    cell.rWall = sharedVertWall
                    cellList[cell_x + 1][cell_y].lWall = sharedVertWall
                if setBot:
                    sharedHorWall = MazeWall()
                    cell.bWall = sharedHorWall
                    cellList[cell_x][cell_y + 1].tWall = sharedHorWall
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

        screenX, screenY = screen_size
        mazeSize = (int(screenX / self.CELL_SIZE),
                    int(screenY / self.CELL_SIZE))
        self.cellList = self.initCells(mazeSize)
        return

    def draw(self):
        for col in self.cellList:
            for cell in col:
                cell.draw(self.mazeScreen)
        return self.mazeScreen
