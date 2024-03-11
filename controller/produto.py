from flask import Blueprint, redirect, render_template, request, url_for

from ext.database import db
from models import Produto, Setor

bp_produto = Blueprint('produto', __name__, template_folder="templates")


@bp_produto.route('/listaProduto')
def listaProduto():
    produtos = Produto.query.all()
    return render_template('listaProduto.html', produtos=produtos)


@bp_produto.route('/create', methods=['GET', 'POST'])
def create():
    setores = Setor.query.all()

    if request.method == 'GET':
        return render_template('produto_create.html', setores=setores)
    elif request.method == 'POST':
        ## Colocar os outros campos de Produto
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        setor_id = request.form.get('setor')

        prod = Produto()  # intancia objeto

        prod.nome = nome
        prod.categoria = categoria
        prod.descricao = descricao
        prod.preco = preco
        prod.quantidade = quantidade
        prod.setor_id = setor_id

        db.session.add(prod)  # add no banco
        db.session.commit()
        return redirect(url_for('produto.listaProduto'))


@bp_produto.route('/delete/<id>', methods=['GET'])
def delete(id):
    if request.method == 'GET':
        produto = Produto.query.filter_by(id=id).first()

        if not produto:
            return 'Não encontrado', 404

        db.session.delete(produto)
        db.session.commit()

        return redirect(url_for('produto.listaProduto'))



@bp_produto.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    prod = Produto.query.filter_by(id=id).first()

    if not prod:
        return 'Não encontrado', 404

    setores = Setor.query.all()

    if request.method == 'GET':
        return render_template('produto_update.html', setores=setores, produto=prod)
    elif request.method == 'POST':
        ## Colocar os outros campos de Produto
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        setor_id = request.form.get('setor')

        prod.nome = nome
        prod.categoria = categoria
        prod.descricao = descricao
        prod.preco = preco
        prod.quantidade = quantidade
        prod.setor_id = setor_id

        db.session.commit()

        return redirect(url_for('produto.listaProduto'))
