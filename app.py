from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    title = "Home"
    lista = [{"Nombre":"Antonio", "Placa":"8989898","Hora":"", "img":"https://i0.wp.com/grupometropoli.net/wp-content/uploads/2018/11/placas-de-nuevo-leon.jpg?fit=700%2C349&ssl=1"},
    {"Nombre":"Jose", "Placa":"8358240","Hora":"", "img":"https://i0.wp.com/grupometropoli.net/wp-content/uploads/2018/11/placas-de-nuevo-leon.jpg?fit=700%2C349&ssl=1"},
    {"Nombre":"Angel", "Placa":"3874983","Hora":"", "img":"https://i0.wp.com/grupometropoli.net/wp-content/uploads/2018/11/placas-de-nuevo-leon.jpg?fit=700%2C349&ssl=1"}]
    return render_template("index.html", 
    title=title, 
    lista = lista,
    listalen = len(lista))
@app.route("/crear")
def crear():
    return render_template("crear.html")

@app.route("/Graficas")
def grafica():
    return render_template("graficas.html")

@app.route("/Ingresar")
def ingresar():
    return render_template("ingresar.html")

@app.route("/Dashboard")
def dashboard():
    return render_template("dashboard.html")

from routes.google import *

if __name__ == "__main__":
    app.run(debug=True)