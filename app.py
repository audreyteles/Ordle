from flask import Flask

app = Flask(__name__)

app.secret_key = 'super secret key'


from views import *

if __name__ == '__main__':
    app.run(debug=False)
