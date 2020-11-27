import numpy as np

'''
units: SI
metric (+---)
X = (ct, x, y, z)
'''

c = 300000000
g = np.array([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1]
])


class FourVector:
    def __init__(self, ct=0, x=0, y=0, z=0, r=None, fourv=None):
        self.pos = np.array([ct, x, y, z]) if r is None and fourv is None else np.array(
            [ct, r[0], r[1], r[2]]) if fourv is None else fourv

    def __repr__(self):
        return f"({self.pos[0]}, {self.pos[1]}, {self.pos[2]}, {self.pos[3]})"

    def __str__(self):
        return self.__repr__()

    def __add__(self, b):
        if isinstance(b, FourVector):
            return FourVector(fourv=(self.pos + b.pos))

    def __iadd__(self, b):
        if isinstance(b, FourVector):
            self.pos = self.pos + b.pos
            return self

    def __radd__(self, b):
        return self.__add__(b)

    def __sub__(self, b):
        if isinstance(b, FourVector):
            return FourVector(fourv=(self.pos - b.pos))

    def __isub__(self, b):
        if isinstance(b, FourVector):
            self.pos = self.pos - b.pos
            return self

    def __rsub__(self, b):
        return self.__sub__(b)

    def __mul__(self, k):
        if isinstance(k, int) or isinstance(k, float):
            new = k * self.pos
            return FourVector(fourv=new)
        else:
            raise "multiplication is defined only for scalars"

    def __imul__(self, k):
        if isinstance(k, int) or isinstance(k, float):
            self.pos = k * self.pos
            return self
        else:
            raise "multiplication is defined only for scalars"

    def __rmul__(self, k):
        return self.__mul__(k)

    def printnormed(self):
        return f"({self.pos[0] / c}, {self.pos[1]}, {self.pos[2]}, {self.pos[3]})"

    def LorentzTransformation(self, v):
        (vx, vy, vz) = v
        V = np.sqrt(vx**2 + vy**2 + vz**2)
        bx, by, bz = beta(vx), beta(vy), beta(vz)
        B = beta(V)
        f = gamma(V)
        l = np.array([
            [f, -f * bx, -f * by, -f * bz],
            [-f * bx, 1 + (f - 1) * (bx**2) / (B**2), (f - 1) *
             (bx * by) / (B**2), (f - 1) * (bx * bz) / (B**2)],
            [-f * by, (f - 1) * (by * bx) / (B**2), 1 + (f - 1) *
             (by**2) / (B**2), (f - 1) * (by * bz) / (B**2)],
            [-f * bz, (f - 1) * (bz * bx) / (B**2), (f - 1) *
             (bz * by) / (B**2), 1 + (f - 1) * (bz * bz) / (B**2)]
        ])

        new = l.dot(self.pos)

        return FourVector(new[0], new[1], new[2], new[3])

    def LorentzXT(self, v):
        f = gamma(v)
        b = beta(v)
        mat = np.array([
            [f, - b * f, 0, 0],
            [- b * f, f, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        new = mat.dot(self.pos)
        return FourVector(new[0], new[1], new[2], new[3])


def gamma(v):
    return (1 / np.sqrt(1 - (v**2) / (c**2)))


def beta(v):
    return (v / c)


def ds2(a, b):
    return g.dot(a.pos).dot(b.pos)


def VelocityCompToPrime(u, v):
    return ((u - v) / (1 - u * v / c**2))

def VelocityCompToUnprime(U, v):
    return ((U + v) / (1 + U * v / c**2))

a = FourVector(5e-9 * c, 2, 0, 0)
b = FourVector(10e-9 * c, 3, 0, 0)

print(ds2(a-b, a-b))
print((a-b).printnormed())