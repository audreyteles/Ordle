from app import app, db
from flask_migrate import Migrate


migrate = Migrate(app, db)


class Informacao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date)
    nome = db.Column(db.String(45))
    imagem = db.Column(db.String(2048))
    hoje = db.Column(db.Boolean)