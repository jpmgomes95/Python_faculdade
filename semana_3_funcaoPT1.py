import math

raio = float(input("Insira o raio do circulo: "))
x = float(input("Insira a coordenada X: "))
y = float(input("Insira a coordenada Y: "))

class circulo:
    def __init__(self, x, y, raio, perimetro, area, diametro) :
        self.__x = x 
        self.__y = y
        self.__raio = raio
        self.__perimetro = perimetro
        self.__area = area
        self.__diamentro = diametro

    def calculo_area(self):
        self.__area = math.pi * math.pow(self.__raio,2)

    def calculo_perimetro(self):
        self.__perimetro = 2 * math.pi * self.__raio

    def calculo_diametro(self):
        self.__diamentro = self.__raio *2

    def set_raio(self, novoraio):
        self.__raio = novoraio