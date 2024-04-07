from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
import boto3

# componente de banco de dados
db = SQLAlchemy()

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpeg'}

# True para limpar a instancia banco de dados atual
DROP_DATA_BASE = False

# Carrega os valores da credencial de acesso da AWS
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

# Instancia principal da aplicação
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

try: 
    # Componente para acessar o AWS S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    BUCKET_NAME = "my-app-files-bucket"
    print("Componente de acesso ao S3 carregado com sucesso!")
except Exception as ex:
    print(f"Erro ao carregar componente do S3: {str(ex)}")

# Inicializa a instância do banco de dados
db.init_app(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Classe que representa os dados de um arquivo
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_filename = db.Column(db.String(100))
    filename = db.Column(db.String(100))
    bucket = db.Column(db.String(100))
    region = db.Column(db.String(100))

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
@app.route("/bemvindo")
def bem_vindo():
    mensagem = "<p>Bem vindo ao Flask!"
    return mensagem

# Rota principal
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file-to-save"]
        
        if not allowed_file(uploaded_file.filename):
            return "FILE NOT ALLOWED!"

        new_filename = uuid.uuid4().hex + '.' + uploaded_file.filename.rsplit('.', 1)[1].lower()
        s3.upload_fileobj(uploaded_file, BUCKET_NAME, new_filename)
        file = File(original_filename=uploaded_file.filename, filename=new_filename,
            bucket=BUCKET_NAME, region="us-east-1")
        db.session.add(file)
        db.session.commit()

        return redirect(url_for("index"))

    files = File.query.all()

    return render_template("index.html", files=files)

create_tables()

if __name__=='__main__':
    app.run(debug=True)