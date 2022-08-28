from werkzeug.utils import redirect
from app import app, db
from flask import flash, render_template, request, url_for, session
from web_scraping import getLink
from datetime import date
from Models.InformacoesModel import Informacao


@app.route('/', methods=['POST', 'GET', ])
def index():
    global nome, imagem

    session.permanent = True
    data = date.today().strftime("%Y-%m-%d")

    info = Informacao.query.filter_by(data=data).first()
    try:
        nome = info.nome
        imagem = info.imagem
    except:
        pass

    if info is None:
        while True:
            try:
                nome, imagem = getLink()
                existe = Informacao.query.filter_by(nome=nome).first()

                if existe is None:
                    add = Informacao(data=data, nome=nome, imagem=imagem)
                    db.session.add(add)
                    db.session.commit()
                    session['pontos'] = 5
                    session['blur'] = 25
                    break
            except:
                pass
    if session.get('pontos') is None:
        session['pontos'] = 5
        session['blur'] = 25

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
