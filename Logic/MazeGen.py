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
        # * Still bit buggy
        # ** Opens up edges, should not be possible
        # ** Doesn't seem to open up every wall
        aimList = [aim for aim in Aim]
        shuffle(aimList)

        moved = False
        while aimList and not moved:
            aim = aimList.pop()
            nextPos = move(self.currPos, aim)

            # Cell/direction has to be within bounds and unvisited
            if nextPos in self.visited.keys() and not self.visited[nextPos]:

                print("Opening from: ", self.currPos, " towards: ", aim)
                self.mazeRef.open(self.currPos, aim)
                self.currPos = nextPos
                self.currWalk.append(nextPos)
                self.visited[nextPos] = True
                moved = True

        if not moved:
            # All neigbors already visited. Backtrack and try again
            self.currPos = self.currWalk.pop()
            self.NextStep()

        # time.sleep(0.1)

        pass
