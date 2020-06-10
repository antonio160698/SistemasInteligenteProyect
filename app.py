from flask import Flask, render_template
app = Flask(__name__)

@app.route("/reports")
def index():
    title = "Home"
    lista = [
    {"Nombre":"Jose Antonio Torres Garibay", "Zona": "A6", "Placa":"K56-AFK", "Fecha":"10/06/2020", "img":"https://cdn-3.expansion.mx/dims4/default/bd2f85d/2147483647/strip/true/crop/1200x801+0+0/resize/800x534!/quality/90/?url=https%3A%2F%2Fcherry-brightspot.s3.amazonaws.com%2Ff7%2F6a%2Fd2dc8c124361883a407bc7bc0e4d%2Fcambio-placas-1.jpg-1%20%281%29.jpg"},
    {"Nombre":"Jose Miguel Salazar Ramirez", "Zona": "C22", "Placa":"GZA-39-94", "Fecha":"10/06/2020", "img":"https://media.metrolatam.com/2019/06/03/placas-e15245428559abe9a67bb7a0d9b96204-1200x800.jpg"},
    {"Nombre":"Angel Abdiel Jimenez Garza", "Zona": "D3", "Placa":"UNK-028", "Fecha":"11/06/2020", "img":"https://live.staticflickr.com/8002/7446223590_a650a0d7e5_b.jpg"}]
    return render_template("index.html", 
    title=title, 
    lista = lista,
    listalen = len(lista))

@app.route("/reports/<id>")
def show(id):
    objects_list = [
    {"Nombre":"Jose Antonio Torres Garibay", "Zona": "A6", "Placa":"K56-AFK", "Fecha":"10/06/2020", "img":"https://cdn-3.expansion.mx/dims4/default/bd2f85d/2147483647/strip/true/crop/1200x801+0+0/resize/800x534!/quality/90/?url=https%3A%2F%2Fcherry-brightspot.s3.amazonaws.com%2Ff7%2F6a%2Fd2dc8c124361883a407bc7bc0e4d%2Fcambio-placas-1.jpg-1%20%281%29.jpg"},
    {"Nombre":"Jose Miguel Salazar Ramirez", "Zona": "C22", "Placa":"GZA-39-94", "Fecha":"10/06/2020", "img":"https://media.metrolatam.com/2019/06/03/placas-e15245428559abe9a67bb7a0d9b96204-1200x800.jpg"},
    {"Nombre":"Angel Abdiel Jimenez Garza", "Zona": "D3", "Placa":"UNK-028", "Fecha":"11/06/2020", "img":"https://live.staticflickr.com/8002/7446223590_a650a0d7e5_b.jpg"}]
    return render_template("show.html", object=objects_list[int(id)])

@app.route("/reports/new")
def crear():
    return render_template("crear.html")

@app.route("/graphs")
def grafica():
    return render_template("graficas.html")

@app.route("/")
def ingresar():
    return render_template("ingresar.html")

@app.route("/home")
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
