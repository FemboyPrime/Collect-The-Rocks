import pygame
import simpleGE
import random

class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("images/spaceship-png-icon-19.png")
        self.setSize(100, 100)
        self.position = (200, 400)
        self.move_speed = 10      

    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.move_speed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.move_speed
        if self.isKeyPressed(pygame.K_w):
            self.y -= self.move_speed
        if self.isKeyPressed(pygame.K_s):
            self.y += self.move_speed 

class Asteroids (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("images/asteroid.png")
        self.setSize(50, 50)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
   
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
class Score_Label(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class Timer_Label(simpleGE.Label):
      def __init__(self):
        super().__init__()
        self.text = "Time Left: 3"
        self.center = (500, 40)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Collect the Rocks")

        # Calling the classes here
        self.ship = Ship(self)
        # This is were the score and timer section is going to be
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 3

        self.score_label = Score_Label()

        self.asteroids = []

        self.timer_label = Timer_Label()

        for self.asteroid in range(0, 15):
            self.asteroids.append(Asteroids(self))

        self.sprites = [
            self.ship, 
            self.asteroids, 
            self.score_label,
            self.timer_label
            ]

    def process(self):
        for asteroid in self.asteroids:
            if self.ship.collidesWith(asteroid):
                asteroid.reset()
                self.score += 1
                self.score_label.text = f"Score: {self.score}"
        self.timer_label.text = f"Time Left: {self.timer.getTimeLeft():.0f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()




def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
