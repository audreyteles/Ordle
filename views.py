from werkzeug.utils import redirect
from app import app
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from datetime import date
import json

today = date.today()

@app.route('/', methods=['POST', 'GET', ])
def index():
    session.permanent = True
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
        session['pontos'] = 5
        session['blur'] = 25
        with open('lista.json', 'w') as f:
            nome, imagem = getLink()
            texto = open('anteriores.txt', 'r')
            itens = str(texto.read())

            while nome in itens:
                nome, imagem = getLink()

            lista = ['', nome]

            with open('anteriores.txt', 'a') as linha:
                linha.writelines('\n'.join(lista))

            json.dump({'data': data,
                       'nome': nome,
                       'imagem': imagem}, f, ensure_ascii=False)

    return render_template("layout.html",
                           personagem=nome,
                           imagem=imagem)


@app.route('/autenticar', methods=['POST', 'GET', ])
def autenticar():
    if request.method == 'POST':
        entrada = " " + request.form['entrada'] + " "
        print(nome)
        if entrada.lower() == nome.lower():
            session['blur'] = 0
            flash("Parabéns, você acertou!!")
        else:
            session['pontos'] = session['pontos'] - 1
            session['blur'] = session['blur'] - 5

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
