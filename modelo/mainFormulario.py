import re
import dao.users as users

class formulario:
    def __init__(self, identificador, nombre, cantidad, categorias, ingreso, perecible, tipoVenta):
        self.identificador = identificador
        self.nombre = nombre
        self.cantidad = cantidad
        self.categorias = categorias
        self.ingreso = ingreso
        self.perecible = perecible
        self.tipoVenta = tipoVenta
    
    def __str__(self, identificador, nombre, cantidad, categorias, ingreso, perecible, tipoVenta):
        return f"datos recibidos: {identificador}, {nombre}, {cantidad}, {categorias}, {ingreso}, {perecible}, {tipoVenta}"
    
    def agregar(self):
        users.agregar(self)