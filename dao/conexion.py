import sqlite3

def conectar():
    con = sqlite3.connect('ventas.db')
    return con
    




 