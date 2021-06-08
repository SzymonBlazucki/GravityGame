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
        self.moneySound = pygame.mixer.Sound(moneySound)
        pygame.mixer.music.load(backgroundMusic)
        self.fontName = pygame.font.match_font(fontName)

    def new(self):
        self.allSprites = pygame.sprite.Group()
        self.player = Player(self, initialPosition, initialVelocity)
        self.planets = pygame.sprite.Group()
        self.moneyLeft = len(moneyLoc)
        for p in planet1:
            Planet(self, *p)
        self.money = pygame.sprite.Group()
        for p in moneyLoc:
            Money(self, *p)
        self.allSprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        pygame.mixer.music.play(loops=-1)
        self.showStartScreen()
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()


    def update(self):
        self.allSprites.update()
        # Money collect
        if pygame.sprite.spritecollide(self.player, self.money, True, pygame.sprite.collide_mask):
            self.moneyLeft -= 1
            self.moneySound.play()
            if self.moneyLeft == 0:
                self.playing = False
                pygame.mixer.music.fadeout(4500)
                g.showFinishScreen()
                self.running = False

        # Die condition
        if self.player.rect.top > self.screen.get_height():
            self.dieSound.play()
            self.playing = False
        elif self.player.rect.bottom < 0:
            self.playing = False
            self.dieSound.play()
        elif self.player.rect.left > self.screen.get_width():
            self.playing = False
            self.dieSound.play()
        elif self.player.rect.right < 0:
            self.playing = False
            self.dieSound.play()
        elif pygame.sprite.spritecollide(self.player, self.planets, False, pygame.sprite.collide_mask):
            self.playing = False
            self.dieSound.play()

    def showStartScreen(self):
        # game splash/start screen
        self.screen.fill(backgroundColor)
        self.drawText("Galaxy escape", 48, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height() / 4))
        self.drawText("Use side thrusters with left and right arrow, up for a main thruster", 22, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height() / 2))
        self.drawText("Press a key to play", 22, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height()* 3 / 4))
        pg.display.flip()
        self.waitForKey()

    def showFinishScreen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(backgroundColor)
        self.drawText("GAME OVER", 48, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height() / 4))
        self.drawText("Score: " + str(self.money), 22, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height() / 2))
        self.drawText("Press a key to play again", 22, colors["white"], math.floor(self.screen.get_width()/2), math.floor(self.screen.get_height()*3 / 4))
        pg.display.flip()
        self.waitForKey()

    def waitForKey(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(backgroundColor)
        self.allSprites.draw(self.screen)
        self.drawText("Avoid planets and collect all coins to win", 25,
                      colors["black"], math.floor(self.screen.get_width()/2), 50)
        pygame.display.flip()

    def drawText(self, text, size, color, x, y):
        font = pygame.font.Font(self.fontName, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        self.screen.blit(textSurface, textRect)

# running the game
g = Game()
while g.running:
    g.new()

pygame.quit()

