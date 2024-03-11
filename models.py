from sqlalchemy_serializer import SerializerMixin

from ext.database import db


class Setor(db.Model):
    __tablename__ = "setor"

    id = db.Column(db.Integer, primary_key=True)
    nomeSetor = db.Column(db.String(150), nullable=False)
    produtos = db.relationship('Produto', backref='setor')


class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(300), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    setor_id = db.Column(db.Integer, db.ForeignKey('setor.id'))
