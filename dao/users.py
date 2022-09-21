import re
import dao.conexion as conexion

def conectar():
    con = conexion.conectar()
    return con

#agrega datos del formulario
def agregar(f):
    conn = conectar()
    cursor = conn.cursor()
    sql = ("INSERT INTO datosVentas (identificador, nombre, cantidad, categorias, ingreso, perecible, tipoVenta) VALUES (?, ?, ?, ?, ?, ?, ?)")
    datos = [f.identificador, f.nombre, f.cantidad, f.categorias, f.ingreso, f.perecible, f.tipoVenta]
    cursor.execute(sql, datos)
    cursor.close()
    conn.commit()
    
    print("datos agregados")