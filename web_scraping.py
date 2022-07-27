from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from random import randrange

def tratarHtml(url):
    response = urlopen(url)
    html = response.read()

    # Tratamento do html
    html = html.decode("utf-8")
    replaced = " ".join(html.split()).replace("> <", "><")
    return bs(replaced, 'html.parser')


def getLink():
    soup = tratarHtml("https://ordemparanormal.fandom.com/wiki/Personagens")

    # Criando lista com os liks para cada página de personagens
    lista = soup.findAll("div", {"class":"moldura-link"})

    # Sorteia uma das páginas de personagens da lista para pegar o link
    soup = tratarHtml("https://ordemparanormal.fandom.com" + lista[randrange(0, len(lista)-1)].a["href"])

    # Lista as imagens de "perfil dos personagens"
    lista = soup.findAll("img", {"class":"pi-image-thumbnail"})

    imagem = lista[len(lista) -1]["src"].replace("static", "vignette")

    # Retorna o nome do perfil e a imagem de "perfil" mais recente
    return soup.h1.getText(), imagem
