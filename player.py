import pygame as pg
import pygame.sprite
import math

from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos, vel):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(rocketImage)
        self.image = pygame.transform.scale(self.image, (math.floor(self.image.get_width()*0.2), math.floor(self.image.get_height()*0.45)))
        self.mask = pygame.mask.from_surface(self.image)
        self.imageStart = self.image
        self.angle = initialAngle
        self.rect = self.image.get_rect()
        self.pos = vec(pos[0], pos[1])
        self.vel = vec(vel[0], vel[1])
        self.omega = 0

    def getThrusterAccel(self):
        ownFrameAccel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ownFrameAccel.x -= sideThrusterA
        if keys[pygame.K_RIGHT]:
            ownFrameAccel.x += sideThrusterA
        if keys[pygame.K_UP]:
            ownFrameAccel.y -= mainThrusterA
        return ownFrameAccel.rotate(-self.angle)

    def getGravityAccel(self):
        gravityAccel = vec(0, 0)
        for p in self.game.planets:
            relativePos = self.pos - p.getPosition()
            gravityAccel -= p.gravity * relativePos.normalize() / relativePos.magnitude_squared()
        return gravityAccel

    def getAccel(self):
        return self.getThrusterAccel() + self.getGravityAccel()

    def getAlpha(self):
        alpha = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            alpha -= sideThrusterAlpha
        if keys[pygame.K_RIGHT]:
            alpha += sideThrusterAlpha
        return alpha

    def update(self):
        self.omega += self.getAlpha() * timeStep
        dVel = self.getAccel() * timeStep
        angleDiff = self.omega * timeStep
        self.vel += dVel
        # print(self.vel.angle_to(vec(0,-1)) , self.angle)
        self.angle -= angleDiff
        self.image = pygame.transform.rotozoom(self.imageStart, self.angle, 1)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos += self.vel * timeStep
        self.rect.center = self.pos


class Planet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, gravity, name, scale):
        self.groups = game.allSprites, game.planets
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.image = pygame.image.load(name)
        self.image = pygame.transform.scale(self.image, (math.floor(self.image.get_rect().width * scale),
                                                         math.floor(self.image.get_rect().width * scale)))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.gravity = gravity

    def getPosition(self):
        return self.rect.center

class Money(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites, game.money
        pygame.sprite.Sprite.__init__(self, *self.groups)
        self.image = pygame.image.load(moneyName)
        self.image = pygame.transform.scale(self.image, (math.floor(self.image.get_rect().width * 0.05),
                                                         math.floor(self.image.get_rect().width * 0.05)))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y