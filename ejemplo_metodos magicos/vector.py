import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return NotImplemented

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __len__(self):
        return int(round(math.sqrt(self.x**2 + self.y**2 + self.z**2)))

    def __eq__(self, other):
        return isinstance(other, Vector3D) and self.x == other.x and self.y == other.y and self.z == other.z
