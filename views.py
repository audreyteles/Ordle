from urllib.request import urlopen, Request
from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from localStoragePy import localStoragePy
import time
nome = ""
imagem = ""
app.secret_key = 'super secret key'
localStorage = localStoragePy('app', 'json')
valor = 0
@app.get("/")
def index():

    if session.get('pontos') is None:
        session['pontos'] = 5
        session['blur'] = 25



    global nome, imagem
    global valor
    if int(time.strftime("%H")) > 0 and valor ==0:

            valor = valor + 1
            session['pontos'] = 5
            session['blur'] = 25
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
        session['blur'] = 0
        flash("Parabéns, você acertou!!")

    else:
        session['pontos'] = session['pontos'] - 1
        session['blur'] = session['blur'] - 5
        localStorage.setItem('pontos', int(localStorage.getItem('pontos'))-1)
        localStorage.setItem('blur', int(localStorage.getItem('blur'))-5)

    return redirect(url_for('index'))
