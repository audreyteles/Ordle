from flask import Flask

app = Flask(__name__)
nome = ""
imagem = ""
app.secret_key = 'super secret key'
valor = 0

from views import *

if __name__ == '__main__':
    app.run(debug=True)