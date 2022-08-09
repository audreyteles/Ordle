from urllib.request import urlopen, Request
from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from datetime import date
import json

valor = 0
today = date.today()


@app.route('/', methods=['POST', 'GET',])
def index():
    data = today.strftime("%d/%m")

    if session.get('pontos') is None:
        session['pontos'] = 5
        session['blur'] = 25

    global nome, imagem

    personagem = open('lista.json')
    dados = json.load(personagem)

    if data == dados['data']:
        nome = dados['nome']
        imagem = dados['imagem']

    else:
        with open('lista.json', 'w') as f:
            session['pontos'] = 5
            session['blur'] = 25
            nome, imagem = getLink()
            json.dump({'data': data,
                       'nome': nome,
                       'imagem': imagem}, f, ensure_ascii=False)

    return render_template("template.html",
                           personagem=nome,
                           imagem=imagem)


@app.route('/autenticar', methods=['POST', 'GET',])
def autenticar():
    if request.method == 'POST':
        entrada = " " + request.form['entrada'] + " "
        if entrada.lower() == nome.lower():
            session['blur'] = 0
            flash("Parabéns, você acertou!!")

        else:
            session['pontos'] = session['pontos'] - 1
            session['blur'] = session['blur'] - 5

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
