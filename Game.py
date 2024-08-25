from pygame import Vector2

from Ball import Ball
from Ring import Ring
from Sounds import sounds
from utils import utils


class Game:
    def __init__(self):
        self.ball = Ball(Vector2(utils.width/2,utils.height/2),1,(255,255,255))
        self.rings = [
            Ring(Vector2(utils.width / 2, utils.height / 2), 22,1,4),
            Ring(Vector2(utils.width / 2, utils.height / 2), 15,-1,3),
            Ring(Vector2(utils.width / 2, utils.height / 2), 25, -1, 360),
        ]

    def update(self):
        utils.world.Step(1.0 / 60.0, 6, 2)
        if utils.contactListener:
            for bodyA,bodyB in utils.contactListener.collisions:
                sounds.play()
                break
            utils.contactListener.collisions = []

    def draw(self):
        for ring in self.rings:
            ring.draw()
        self.ball.draw()