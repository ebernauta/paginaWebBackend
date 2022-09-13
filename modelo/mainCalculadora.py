import dao.calculos as calculos

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"valor 1: {self.a}\nvalor 2: {self.b}"
        
    
    def sumar(self):
        calculos.sumar(self)
    
    def restar(self):
        calculos.restar(self)
        

    def multiplicar(self):
        calculos.multiplicar(self)
        

    def dividir(self):
        calculos.dividir(self)

        