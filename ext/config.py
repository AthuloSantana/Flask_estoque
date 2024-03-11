def init_app(app):
    conexao = "sqlite:///autoBanc.sqlite"
    app.config['SECRET_KEY'] = 'padrao'
    app.config['SQLALCHEMY_DATABASE_URI'] = conexao
    app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
