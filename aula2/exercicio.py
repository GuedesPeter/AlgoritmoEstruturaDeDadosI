'''
Construa um algoritmo para implementar a
classe Retângulo que possui os atributos: altura
e largura.
A classe deve ter os seguintes métodos:
-  Método construtor
- Método que calcula a área do retângulo
( altura * largura) e retorna o resultado
- Método que imprime os valores dos atributos
da classe.
'''


class Retangulo:
    def __init__(self):
        self.altura = float(input('Digite a altura do Retângulo: '))
        self.largura = float(input('Digite a largura do Retângulo: '))

    def calcular_area(self):
        area = (self.altura * self.largura)
        return area
    
    def imprimir_dados(self):
        return print(f' ALTURA: {self.altura} - LARGURA: {self.largura} - ÁREA: {self.calcular_area()} m².')


r1 = Retangulo()
r1.calcular_area()
r1.imprimir_dados()
