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
    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    ## for the ~ operator
    def __ne__(self):
        return Vec3(-1 * self.e[0], -1 * self.e[1], -1 * self.e[2])

    # for accessing using []
    def __class_getitem__(self, i):
        return self.e[i]

    # for /=
    def __idiv__(self, t):
        return self.__imul__(1 / t)

    # vector utility functions
    def print(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    # adding 2 vectors
    def __add__(self, other):
        return Vec3(
            self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2]
        )

    ## subtracting 2 vectors
    def __sub__(self, other):
        return Vec3(
            self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2]
        )

    ## mutliplying 2 vectors together
    def __mul__(self, other):
        return Vec3(
            self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2]
        )

    ## scale up
    def _scale_mul(self, t):
        return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)

    ## scale down
    def _scale_up(self, t):
        return (1 / t) * self.e

    # dot product
    def dot(self, other):
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

    # cross product
    def cross(self, other):
        return Vec3(
            self.e[1] * other.e[1] - self.e[2] * other.e[1],
            self.e[2] * other.e[0] - self.e[0] * other.e[2],
            self.e[0] * other.e[1] - self.e[1] * other.e[0],
        )

    # return the unit_vector of a given vector
    def unit_vector(self):
        return self.e / self.length()


## defining a color utility function
def write_color(pixel_color):
    res = (
        Vec3.print(int(255.999 * pixel_color.x()))
        + " "
        + Vec3.print(int(255.999 * pixel_color.y()))
        + " "
        + Vec3.print(int(255.999 * pixel_color.z()))
    )
    return res

