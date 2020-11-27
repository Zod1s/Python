import math, pygame
from numpy import around, pi
from sys import exit
#import pyparticles

width = 0
height = 0
screen = None
G = 1

class Vec2d:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_angle(rho, theta):
        x = rho * math.cos(theta)
        y = rho * math.sin(theta)
        return Vec2d(x, y)

    # overriding methods

    def __add__(self, other):
        if isinstance(other, Vec2d) or isinstance(other, list) or isinstance(other, tuple):
            x = self.x + other[0]
            y = self.y + other[1]
            return self.__class__(x, y)
        else:
            exit("Impossibile sommare un vettore e un non vettore")

    def __radd__(self, other):
        return self.__add__(other)
    
    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vec2d) or isinstance(other, list) or isinstance(other, tuple):
            x = self.x - other[0]
            y = self.y - other[1]
            return self.__class__(x, y)
        else:
            exit("Impossibile sottrarre un vettore e un non vettore")

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return self.__class__(x, y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, (int, float)):
            try:
                x = self.x / other
                y = self.y / other
                return self.__class__(x, y)
            except:
                exit("Divisione per zero")

    def __rdiv__(self, other):
        exit("Impossibile dividere per un vettore")

    def __idiv__(self, other):
        return self.__div__(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __len__(self):
        return self.__abs__()

    def __getitem__(self, key):
        return self.x if key == 0 else self.y if key == 1 else exit("Indice fuori dai limiti")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            exit("Indice fuori dai limiti")

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __neq__(self, other):
        return not self.__eq__(other)

    def __int__(self):
        return (int(around(self.x, decimals=0)), int(around(self.y, decimals=0)))

    def __str__(self):
        return f"({self.x}, {self.y})"

    # new methods

    def zero(self):
        self.x = self.y = 0

    def arg(self, angle):
        l = abs(self)
        self.x = l * math.cos(angle)
        self.y = l * math.sin(angle)

    def get_angle(self):
        return math.atan2(self.y, self.x)

    def set_length(self, length):
        l = abs(self)
        self.x *= length / l
        self.y *= length / l

    def create_copy(self):
        return Vec2d(self.x, self.y)

class Particle:
    __slots__ = 'pos', 'vel', 'acc', 'mass', 'colour', 'radius'

    def __init__(self, x, y, velmag, veldir, mass, colour, radius):
        self.pos = Vec2d(x, y)
        self.vel = Vec2d(velmag * math.cos(veldir), velmag * math.sin(veldir))
        self.acc = Vec2d(0, 0)
        self.mass = mass
        self.colour = colour
        self.radius = radius

    def gravForce(self, others):
        """returns an array with the indexes of the particles to remove"""
        total_force = Vec2d(0, 0)

        to_remove = []

        for index, other in enumerate(others):
            pos = self.pos - other.pos
            d = len(pos)
            if math.isclose(d, 0):
                self.mass += other.mass
                to_remove.append(index)
            else:
                u = pos / d
                F = - G * self.mass * other.mass * u / d**2
                total_force += F

        self.preapplyforce(total_force)

        return to_remove

    def collide(self, particle2):
        def dot_prod(a, b):
            return a.x * b.x + a.y * b.y

        dX = self.pos - particle2.pos

        if abs(dX) < self.radius + particle2.radius:
            v1 = self.vel.create_copy()
            v2 = particle2.vel.create_copy()

            self.vel = v1 - ((2 * particle2.mass) * dot_prod(v1 - v2, dX) * (dX))\
                            / ((self.mass + particle2.mass) * abs(dX)**2)

            dX *= -1

            particle2.vel = v2 - ((2 * self.mass) * dot_prod(v2 - v1, dX) * (dX))\
                            / ((self.mass + particle2.mass) * abs(dX)**2) 

    def preapplyforce(self, F):
        F /= self.mass
        self.acc.x = F.x
        self.acc.y = F.y

    def refresh(self, items):
        for item in items:
            if item != self:
                self.collide(item)

        self.check_pos()
        self.vel += self.acc
        self.pos += self.vel

    def check_pos(self):
        if self.pos.x < self.radius or self.pos.x > width - self.radius:
            self.vel.x *= -1
            self.pos.x = self.radius if self.pos.x < self.radius else width - self.radius

        if self.pos.y < self.radius or self.pos.y > height - self.radius:
            self.vel.y *= -1
            self.pos.y = self.radius if self.pos.y < self.radius else height - self.radius

    def show(self):
        pygame.draw.circle(screen, self.colour, int(self.pos), self.radius)