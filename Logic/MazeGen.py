from random import randrange
from random import shuffle
from Logic.Move import Aim
from Logic.Move import move


class celRef:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.visited = False


class MazeGen:
    def initRefList(self, cellList):

        refList = []
        for col in cellList:
            colList = []

            for cell in col:
                colList.append(celRef(cell.pos))

            refList.append(colList)

        return refList

    def __init__(self, maze) -> None:
        self.refList = self.initRefList(maze.cellList)
        self.mazeRef = maze
        self.currPos = maze.startEnd[0]
        self.startPos = maze.startEnd[0]
        self.endPos = maze.startEnd[1]
        self.currWalk = {maze.startEnd[0]}

    def NextStep(self):
        # TODO:
        # * Actually call this function and perform a couple of steps through the maze
        # * Implement the correct algorithm for maze generation
        # ** Check cells if you've visited them before moving to them
        # ** Add backtracking functionality
        #
        aimList = [aim for aim in Aim]
        aimList.shuffle()

        moved = False
        aim = None
        while aimList and not moved:  # Check if already visited
            aim = aimList.pop()
            moved = self.mazeRef.open(self.currPos, aim)

        if moved:
            self.currPos = move(self.currPos, aim)
            self.currWalk.add(self.currPos)
            # Handle not moving at all --> all neighbors visited --> backtrack and start new walk

        pass
