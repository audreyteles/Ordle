from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.secret_key = os.environ['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=False)
