from urllib.request import urlopen, Request
from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink

nome = ""
imagem = ""

class Usuario:
    def __init__(self):
        self.pontos = 5

    def setPontos(self):
        self.pontos =- 1

    def getPontos(self):
        return self.pontos

user = Usuario()

@app.get("/")
def index():
    global nome, imagem
    if nome == "" and imagem == "":
        session['blur'] = 25
        session['pontos'] = 5
        nome, imagem = getLink()

    return render_template("template.html",
                           personagem=nome,
                           imagem=imagem,
                           blur=10,
                           pontos=5)


@app.post('/autenticar')
def autenticar():
    entrada = " " + request.form['entrada'] + " "
    print(nome)
    if entrada.lower() == nome.lower():
        flash("Parabéns, você acertou!!")
    else:
        session['pontos'] = session['pontos'] - 1
        session['blur'] = session['blur'] - 5
        flash("Errou.", "error")

    return redirect(url_for('index'))
