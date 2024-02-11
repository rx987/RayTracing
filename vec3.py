import math


class Vec3:
    e = []

    def __init__(self, e1, e2, e3):
        self.e = [e1, e2, e3]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    ## for the += operator
    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    ## for the *= operator
    def __imul__(self, other):
        self.e[0] *= other.e[0]
        self.e[1] *= other.e[1]
        self.e[2] *= other.e[2]
        return self

    ## for the ~ operator
    def __ne__(self):
        return Vec3(-1 * self.e[0], -1 * self.e[1], -1 * self.e[2])
    
    
