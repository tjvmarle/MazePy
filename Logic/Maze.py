import pygame


class Maze:
    def __init__(self, screen_size):
        """
        Class for making a maze
        """

        self.mazeScreen = pygame.Surface(screen_size)
        self.mazeScreen.fill((200, 200, 200))

        pass
