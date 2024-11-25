import pygame
import simpleGE


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Test")        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
