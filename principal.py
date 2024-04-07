from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def bem_vindo():
    mensagem = "<p>Bem vindo ao Flask!"
    return mensagem

@app.route("/home")
def home_page():
    return render_template("home.html")