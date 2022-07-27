from urllib.request import urlopen, Request
from app import app
from flask import render_template
from web_scraping import getLink

@app.get("/")
def index():
    nome,imagem = getLink()
    return render_template("template.html",
                           personagem=nome,
                           imagem=imagem,
                           blur=15)
@app.post('/autenticar')
def autenticar():
    return ""