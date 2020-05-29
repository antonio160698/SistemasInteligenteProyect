from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    title = "Home"
    lista = [
    {"Nombre":"Antonio", "Placa":"k56-afk","Hora":"", "img":"https://cdn-3.expansion.mx/dims4/default/bd2f85d/2147483647/strip/true/crop/1200x801+0+0/resize/800x534!/quality/90/?url=https%3A%2F%2Fcherry-brightspot.s3.amazonaws.com%2Ff7%2F6a%2Fd2dc8c124361883a407bc7bc0e4d%2Fcambio-placas-1.jpg-1%20%281%29.jpg"},
    {"Nombre":"Jose", "Placa":"gza-39-94","Hora":"", "img":"https://media.metrolatam.com/2019/06/03/placas-e15245428559abe9a67bb7a0d9b96204-1200x800.jpg"},
    {"Nombre":"Angel", "Placa":"unk-028","Hora":"", "img":"https://live.staticflickr.com/8002/7446223590_a650a0d7e5_b.jpg"}]
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

@app.route("/iframe/Dashboard")
def iframedash():
    return render_template("frames/iframegraphs.html")

@app.route("/iframe/list")
def iframelist():
    lista = [
    {"Nombre":"Antonio", "Placa":"k56-afk","Hora":"", "img":"https://cdn-3.expansion.mx/dims4/default/bd2f85d/2147483647/strip/true/crop/1200x801+0+0/resize/800x534!/quality/90/?url=https%3A%2F%2Fcherry-brightspot.s3.amazonaws.com%2Ff7%2F6a%2Fd2dc8c124361883a407bc7bc0e4d%2Fcambio-placas-1.jpg-1%20%281%29.jpg"},
    {"Nombre":"Jose", "Placa":"gza-39-94","Hora":"", "img":"https://media.metrolatam.com/2019/06/03/placas-e15245428559abe9a67bb7a0d9b96204-1200x800.jpg"},
    {"Nombre":"Angel", "Placa":"unk-028","Hora":"", "img":"https://live.staticflickr.com/8002/7446223590_a650a0d7e5_b.jpg"}]
    return render_template("frames/iframelist.html", 
    lista = lista,
    listalen = len(lista))

from routes.google import *

if __name__ == "__main__":
    app.run(debug=True)