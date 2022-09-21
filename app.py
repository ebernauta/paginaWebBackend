import re
from flask import Flask, render_template, request, redirect, url_for
import modelo.mainCalculadora as mainCalculadora
import dao.conexion as conexion
import modelo.mainFormulario as mainFormulario
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/formularioEnviado", methods=["GET", "POST"])
def reciboFormulario():
    identificador = request.form["identificador"]
    nombre = request.form["nombre"]
    cantidad = request.form["cantidad"]
    categorias = request.form["categorias"]
    ingreso = request.form["ingreso"]
    perecible = request.form["eleccion"]
    tipoVenta = request.form["opcion"]
    
    f = mainFormulario.formulario(identificador, nombre, cantidad, categorias, ingreso, perecible, tipoVenta)
    f.agregar()
    
    return f"datos recibidos: {identificador}, {nombre}, {cantidad}, {categorias}, {ingreso}, {perecible}, {tipoVenta}"

@app.route("/calculadora")
def calculadoraWeb():
    return render_template("calculadora.html")

@app.route("/calcular", methods=["POST", "GET"])
def calcular():
    a = request.form["input1"]
    b = request.form["input2"]
    operacion = request.form["operacion"]
    
    if operacion == "sumar":
        valores = mainCalculadora.calculos.sumar(a,b)
        return render_template("calculadora.html", valor=valores)
    elif operacion == "restar":
        valores = mainCalculadora.calculos.restar(a, b)
        return render_template("calculadora.html", valor=valores)
    elif operacion == "multiplicar":
        valores = mainCalculadora.calculos.multiplicar(a, b)
        return render_template("calculadora.html", valor=valores)
    elif operacion == "dividir":
        valores = mainCalculadora.calculos.dividir(a, b)
        return render_template("calculadora.html", valor=valores)
    else:
        return "Vaya algo salió mal !"
    
    return redirect("calcular")


app.run(debug= True)