from flask import render_template, Flask

from controller.produto import bp_produto
from controller.setor import bp_setor


def init_app(app: Flask):
    app.register_blueprint(bp_produto, url_prefix='/produto')
    app.register_blueprint(bp_setor, url_prefix='/setor')
    app.add_url_rule('/', view_func=index)


def index():
    return render_template('base.html')
