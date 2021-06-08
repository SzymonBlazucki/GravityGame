import pygame as pg
import pygame.sprite

from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos, vel):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(rocketImage)
        self.image = pygame.transform.scale(self.image, (50, 63))
        self.mask = pygame.mask.from_surface(self.image)
        self.imageStart = self.image
        self.angle = initialAngle
        print(self.image.get_size())
        self.rect = self.image.get_rect()
        self.pos = vec(pos[0], pos[1])
        self.vel = vec(vel[0], vel[1])
        self.omega = 0

    def get_accel(self):
        ownFrameAccel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ownFrameAccel.x -= sideThrusterA
        if keys[pygame.K_RIGHT]:
            ownFrameAccel.x += sideThrusterA
        if keys[pygame.K_UP]:
            ownFrameAccel.y -= mainThrusterA
        return ownFrameAccel.rotate(self.angle)

    def get_alpha(self):
        alpha = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            alpha += sideThrusterAlpha
        if keys[pygame.K_RIGHT]:
            alpha -= sideThrusterAlpha
        return alpha

    def update(self):
        self.omega += self.get_alpha() * timeStep
        dVel = self.get_accel() * timeStep
        angleDiff = self.vel.angle_to(self.vel + dVel) + self.omega * timeStep
        self.vel += dVel
        self.angle -= angleDiff
        self.image = pygame.transform.rotozoom(self.imageStart, self.angle, 1)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos += self.vel * timeStep
        self.rect.center = self.pos
        print(self.angle)


class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = gravity

# class Money(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#
