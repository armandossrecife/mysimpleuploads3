from flask import Flask, render_template, request, redirect, url_for, flash
import os
import banco
import s3_handle
import uuid
import utilidades

# True para limpar a instancia banco de dados atual
# Obs: o valor deve ser True na 1a execucao da aplicacao
#      para criar um banco limpo a estrutura limpa das tabelas
DROP_DATA_BASE = False

# Carrega os valores das credenciais de acesso da AWS
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

# Instancia principal da aplicação
app = Flask(__name__)
app.secret_key = 'thisismysecretkeyfrommywebapplication'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

# Inicializa a instância do banco de dados
banco.db.init_app(app)
banco.create_tables(app, DROP_DATA_BASE)

# Carrega o componente S3
s3 = s3_handle.carrega_s3(ACCESS_KEY_ID, SECRET_ACCESS_KEY)

# Rota para a pagina home
@app.route("/")
def home_page():
    return render_template("home.html")

# Rota para a pagina de uploads
@app.route("/upload", methods=["GET", "POST"])
def upload_page():
    if request.method == "POST":
        try: 
            uploaded_file = request.files["file-to-save"]
            
            if not utilidades.allowed_file(uploaded_file.filename):
                flash("Tipo de arquivo não permitido!")
                return redirect(url_for('upload_page'))

            new_filename = uuid.uuid4().hex + '.' + uploaded_file.filename.rsplit('.', 1)[1].lower()
            s3.upload_fileobj(uploaded_file, s3_handle.BUCKET_NAME, new_filename)
            file = banco.File(original_filename=uploaded_file.filename, filename=new_filename,
                bucket=s3_handle.BUCKET_NAME, region=s3_handle.AWS_S3_REGION)
            banco.db.session.add(file)
            banco.db.session.commit()
        except Exception as ex: 
            flash(f"Erro no upload! {str(ex)}")
            return redirect(url_for('upload_page'))

        return redirect(url_for("upload_page"))

    files = banco.File.query.all()

    return render_template("upload.html", files=files)

@app.route("/downloads", methods=["GET"])
def downloads_page():
    files = banco.File.query.all()

    if not files: 
        flash('Nenhum arquivo para download!')
        return redirect(url_for('download_page'))

    return render_template("downloads.html", files=files)

if __name__=='__main__':
    app.run(debug=True)