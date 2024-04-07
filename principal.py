from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# componente de banco de dados
db = SQLAlchemy()

DROP_DATA_BASE = True

# Classe que representa os dados de um arquivo
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_filename = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    bucket = db.Column(db.String(100))
    region = db.Column(db.String(100))

# Instancia principal da aplicação
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

# Inicializa a instância do banco de dados
db.init_app(app)

# Recria as tabelas do banco
def create_tables():
    with app.app_context():
        print('Carrega as tabelas do banco')
        if DROP_DATA_BASE: 
            db.drop_all()
            db.create_all()
            db.session.commit()
        print('Tabelas carregadas com sucesso!')

# Rota base
@app.route("/")
def bem_vindo():
    mensagem = "<p>Bem vindo ao Flask!"
    return mensagem

# Rota principal
@app.route("/home")
def home_page():
    return render_template("home.html")

create_tables()

if __name__=='__main__':
    app.run(debug=True)