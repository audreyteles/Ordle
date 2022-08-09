from urllib.request import urlopen, Request
from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from datetime import date
import json

valor = 0
today = date.today()


@app.get("/")
def index():
    dia = today.strftime("%d")

    if session.get('pontos') is None:
        session['pontos'] = 5
        session['blur'] = 25

    global nome, imagem
    personagem = open('lista.json')
    dados = json.load(personagem)
    if dia == dados['dia']:
        nome = dados['nome']
        imagem = dados['imagem']

    else:
        with open('lista.json', 'w') as f:
            nome, imagem = getLink()
            json.dump({'dia': dia,
                       'nome': nome,
                       'imagem': imagem}, f, ensure_ascii=False)

    return render_template("template.html",
                           personagem=nome,
                           imagem=imagem)


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

    return redirect(url_for('index'))
