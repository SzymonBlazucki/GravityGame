import pygame as pg
import pygame.sprite

from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, vel):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(rocketImage)
        self.imageStart = pygame.image.load(rocketImage)
        # self.image = pygame.transform.scale(self.image, (50, 63))
        self.angle = initialAngle
        print(self.image.get_size())
        self.rect = self.image.get_rect()
        self.pos = vec(pos[0], pos[1])
        self.vel = vec(vel[0], vel[1])
        self.omega = 0
        self.accel = vec(0, 0)

    def update(self):
        self.accel = vec(0, 0)
        self.tempAccel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.tempAccel.x = -sideThrusterA
            self.omega -= sideThrusterAlpha * timeStep
        if keys[pygame.K_RIGHT]:
            self.tempAccel.x = sideThrusterA
            self.omega += sideThrusterAlpha * timeStep
        if keys[pygame.K_UP]:
            self.tempAccel.y = -mainThrusterA
        if keys[pygame.K_SPACE]:  # for debug
            print(self.vel.angle_to(vec(0, -1)))
        # find the angle between y axis upwards and velocity vector
        rotate = self.vel.angle_to(vec(0, -1))
        #to accelerate in appropriate direction
        self.accel = self.tempAccel.rotate(-rotate)
        dVel = self.accel * timeStep
        if self.tempAccel.y != 0:
            print(rotate, self.vel.normalize(), dVel.normalize())
        angleDiff = self.vel.angle_to(self.vel + dVel) #+ self.omega * timeStep
        self.vel += dVel
        # print(self.vel.angle_to(vec(0, -1)))
        self.angle -= angleDiff
        self.image = pygame.transform.rotozoom(self.imageStart, self.angle, 1)
        self.rect = self.image.get_rect()
        self.pos += self.vel * timeStep
        self.rect.center = self.pos


class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, a, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.a = a
