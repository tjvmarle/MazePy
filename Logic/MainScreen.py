import pygame
from Logic.Maze import Maze


class MainScreen:

    def __init__(self, screen_size):
        """
        Container for the main and first level subscreens
        """
        pygame.init()
        pygame.display.set_caption("A maze ing")

        self.mainScreen = pygame.display.set_mode(screen_size)
        self.mainScreen.fill((55, 55, 55))
        self.screenList = []
        maze_x, maze_y = screen_size
        self.maze = Maze((int(maze_x * 0.9), int(maze_y * 0.9)))

        self.mainScreen.blit(self.maze.mazeScreen,
                             (int(maze_x * 0.05), int(maze_y * 0.05)))
        pygame.display.update()
        return

    def AddScreen(self, newScreen):
        self.screenList.append(newScreen)
        pass

    def Tick(self):
        for screen in self.screenList:
            screen.drawAll()

        pygame.display.update()
        return True
