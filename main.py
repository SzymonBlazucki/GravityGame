import pygame, sys, random
from settings import *
import numpy as np
from player import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((width, heigth))
        pygame.display.set_caption('Galaxy escape')
        self.clock = pygame.time.Clock()
        self.running = True
        self.dieSound = pygame.mixer.Sound(crashSound)

    def new(self):
        self.allSprites = pygame.sprite.Group()
        self.player = Player(self, initialPosition, initialVelocity)
        self.planets = pygame.sprite.Group()
        self.planet1 = Planet(*planet1)
        self.planets.add(self.planet1)
        self.allSprites.add(self.player)
        self.allSprites.add(self.planet1)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.allSprites.update()
        # Die condition
        if self.player.rect.top > self.screen.get_height():
            #self.dieSound.play()
            self.playing = False
        elif self.player.rect.bottom < 0:
            self.playing = False
            #self.dieSound.play()
        elif pygame.sprite.spritecollide(self.player, self.planets, False, pygame.sprite.collide_mask):
            self.playing = False
            #self.dieSound.play()


    def startScreen(self):
        pass

    def gameOverScreen(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(backgroundColor)
        self.allSprites.draw(self.screen)
        pygame.display.flip()


g = Game()
while g.running:
    g.new()
    g.gameOverScreen()

pygame.quit()

# pygame.draw.line(windowSurface, blue, (60, 60), (120, 60), 4)
# pygame.draw.line(windowSurface, blue, (120, 60), (60, 120))
# pygame.draw.line(windowSurface, blue, (60, 120), (120, 120), 4)
#
# pygame.draw.circle(windowSurface, blue, (300, 50), 20, 0)
#
# pygame.draw.ellipse(windowSurface, red, (300, 250, 40, 80), 1)
#
# pygame.draw.rect(windowSurface, red, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
