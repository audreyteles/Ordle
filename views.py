from urllib.request import urlopen, Request
from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from localStoragePy import localStoragePy

nome = ""
imagem = ""
localStorage = localStoragePy('app', 'json')
@app.get("/")
def index():
    global nome, imagem

    if imagem == "" and nome == "":
        localStorage.setItem('pontos', 5)
        localStorage.setItem('blur', 25)
        nome, imagem = getLink()

    return render_template("template.html",
                           personagem=nome,
                           imagem=imagem,
                           blur=10,
                           pontos=5,
                           localStorage=localStorage,
                           int=int)


@app.post('/autenticar')
def autenticar():
    entrada = " " + request.form['entrada'] + " "
    print(nome)
    if entrada.lower() == nome.lower():
        flash("Parabéns, você acertou!!")
    else:
        localStorage.setItem('pontos', int(localStorage.getItem('pontos'))-1)
        localStorage.setItem('blur', int(localStorage.getItem('blur'))-5)
        flash("Errou.", "error")

    return redirect(url_for('index'))
