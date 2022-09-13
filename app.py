from flask import Flask, render_template, request, redirect, url_for
import modelo.mainCalculadora as mainCalculadora
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/calculadora")
def calculadoraWeb():
    return render_template("calculadora.html")

@app.route("/calcular", methods=["POST", "GET"])
def calcular():
    a = request.form["input1"]
    b = request.form["input2"]
    #operacion = request.form["operacion"]
    #filtro para saber que opcion eligió (sumar - restar - multiplicar - dividir) para despues hacer
    #los calculos 
    valores = mainCalculadora.calculos.sumar(a,b)
    return f"La operacion es: {valores}"


app.run(debug= True)