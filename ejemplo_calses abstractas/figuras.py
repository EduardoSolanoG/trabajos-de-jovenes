from abc import ABC, abstractclassmethod
import math

class Figura(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi * self.radio ** 2, 2)

    def perimetro(self):
        return round(2 * math.pi * self.radio, 2)

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
