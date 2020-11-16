from random import randrange
from random import shuffle
from Logic.Move import Aim
from Logic.Move import move

import time


class MazeGen:
    def initRefDict(self, cellList):

        refDict = {}
        for col in cellList:
            for cell in col:
                refDict[cell.pos] = False

        return refDict

    def __init__(self, maze) -> None:
        self.visited = self.initRefDict(maze.cellList)
        self.mazeRef = maze
        self.currPos = maze.startEnd[0]
        self.startPos = maze.startEnd[0]
        self.endPos = maze.startEnd[1]
        self.currWalk = [maze.startEnd[0]]

    def NextStep(self):
        if not self.currWalk:
            # Maze generation finished
            return

        # TODO:
        # * Add a bit more branching. Has tendency to create long corridors.
        aimList = [aim for aim in Aim]
        shuffle(aimList)

        moved = False
        while aimList and not moved:
            aim = aimList.pop()
            nextPos = move(self.currPos, aim)

            # Cell/direction has to be within bounds and unvisited
            if nextPos in self.visited.keys() and not self.visited[nextPos]:
                if self.currPos != self.currWalk[-1]:
                    self.currWalk.append(self.currPos)
                
                self.mazeRef.open(self.currPos, aim)
                self.currPos = nextPos
                self.currWalk.append(nextPos)
                self.visited[nextPos] = True
                moved = True

        #Possibly temporary - shows the solution
        if moved:
            dWall = self.mazeRef.cellList[self.currPos[0]][self.currPos[1]].walls[Aim.Down]
            if dWall.isEdge and dWall.isOpen:
                for cellPos in self.currWalk:
                    self.mazeRef.drawCell(cellPos, (153, 204, 153))

        if not moved:
            # All neigbors already visited. Backtrack and try again
            self.currPos = self.currWalk.pop()
            self.NextStep()

    def clr(self, pos, color):
        self.mazeRef.drawCell(pos, color)
        pass