import math

class Calculadora_cientifica:
    def __init__(self) -> None:
        self.ultimo_resultado = None

    def validar(self,x,y = 0):
        if type(x) == str or type(y) == str:
            raise TypeError("Digite apenas Números.")
        
        return None

    def soma(self,x,y):
        self.validar(x,y)
        self.ultimo_resultado = x + y 
        return self.ultimo_resultado

    def subtracao(self,x,y):
        self.validar(x,y)
        self.ultimo_resultado = x - y
        return self.ultimo_resultado

    def multiplicacao(self,x,y):
        self.validar(x,y)
        self.ultimo_resultado = x * y
        return self.ultimo_resultado

    def divisao(self,x,y):
        self.validar(x,y)     
        if y == 0 :
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        else :
            self.ultimo_resultado = x / y
            return self.ultimo_resultado

    def potenciacao(self,x,y):
        self.validar(x,y)
        self.ultimo_resultado = math.pow(x,y)
        return self.ultimo_resultado
    
    def raiz_quadrada(self,x):
        self.validar(x)
        if x < 0:
            raise ValueError("ERRO Números Negativos não posuem Raiz")
        else:
            self.ultimo_resultado = math.sqrt(x)
            return self.ultimo_resultado
        
    def logaritimo_natural(self,x):
        self.validar(x)
        if x <= 0:
            raise ValueError("ERRO Números não positivos não tem logaritimo")
        else:
            self.ultimo_resultado = math.log(x)
            return self.ultimo_resultado
        
    def seno(self, x):
        self.validar(x)
        self.ultimo_resultado = math.sin(math.radians(x))
        return self.ultimo_resultado
    
    def coseno(self, x):
        self.validar(x)
        self.ultimo_resultado = math.cos(math.radians(x))
        return self.ultimo_resultado
    
    def tangente(self, x):
        self.validar(x)
        self.ultimo_resultado = math.tan(math.radians(x))
        if x == 90:
            raise ValueError("ERRO a tangente não existe.")
        return self.ultimo_resultado