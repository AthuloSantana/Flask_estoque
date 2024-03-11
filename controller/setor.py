from flask import Blueprint, render_template, request

from ext.database import db
from models import Setor

bp_setor = Blueprint('setor', __name__, template_folder="templates")


@bp_setor.route('/listaSetor')
def listaSetor():
    setores = Setor.query.all()
    return render_template('listaSetor.html', setores=setores)


@bp_setor.route('/delete/<id>', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        setor = Setor.query.filter_by(id=id).first()

        if not setor:
            return 'Não encontrado', 404

        db.session.delete(setor)
        db.session.commit()

        return 'Apagado', 200


@bp_setor.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('setor_create.html')
    elif request.method == 'POST':
        nomeSetor = request.form.get('nomeSetor')

    setor = Setor()  # intancia objeto
    setor.nomeSetor = nomeSetor

    db.session.add(setor)  # add no banco
    db.session.commit()

    return 'Dados recebidos OK'


@bp_setor.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    setor = Setor.query.filter_by(id=id).first()

    if not setor:
        return 'Não encontrado', 404

    if request.method == 'GET':
        return render_template('setor_update.html', setor=setor)
    elif request.method == 'POST':
        ## Colocar os outros campos de Produto
        nome = request.form.get('nomeSetor')

        setor.nomeSetor = nome

        db.session.commit()

    return 'Dados recebidos OK'
