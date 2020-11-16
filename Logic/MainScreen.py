import pygame
from Logic.Maze import Maze
from Logic.MazeGen import MazeGen


class MainScreen:

    def __init__(self, screen_size):
        """
        Container for the main and first level subscreens
        """
        pygame.init()
        pygame.display.set_caption("A maze ing")

        self.mainScreen = pygame.display.set_mode(
            screen_size)  # Primary screen
        self.mainScreen.fill((55, 55, 55))
        mazeX, mazeY = screen_size
        self.maze = Maze((int(mazeX * 0.9), int(mazeY * 0.9)))

        self.mazeGen = MazeGen(self.maze)
        return

    def Tick(self):
        self.mazeGen.NextStep()
        screenX, screenY = self.mainScreen.get_size()
        self.mainScreen.blit(self.maze.draw(),
                             (int(screenX * 0.05), int(screenY * 0.05)))

        pygame.display.update()
        return
