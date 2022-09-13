import modelo.mainCalculadora as mainCalculadora

def sumar(a, b):
    calculo = a + b
    return f"valor = {calculo}"

def restar(a, b):
    calculo = a - b
    return f"valor = {calculo}"

def multiplicar(a, b):
    calculo = a * b
    return f"valor = {calculo}"

def dividir(a, b):
    calculo = a % b
    return f"valor = {calculo}"