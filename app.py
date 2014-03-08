import cgi
from sqlite3 import dbapi2 as sqlite3
from flask import (
		Flask, render_template, flash,
		url_for, redirect, request, _app_ctx_stack
)

DATABASE = '/tmp/bar.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKBAR_SETTINGS', silent=True)


def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar_bar():
    if request.method == 'POST':
        if '' not in request.form.values():
            db = get_db()
            db.execute('''INSERT INTO bar (
              nome, descricao, endereco, telefone, horario_ini, horario_fin, especialidade) 
              VALUES (?, ?, ?, ?, ?, ?, ?)''',
              [request.form.get("nome_bar"), request.form.get("descricao_bar"),
               request.form.get("endereco"), request.form.get("telefone"), request.form.get("horario_ini"), 
               request.form.get("horario_fin"), request.form.get("especialidade")])
            db.commit()
            flash('Bar cadastrado com sucesso!')
            redirect('index.html')
    return render_template('cadastro.html')

@app.route("/")
def exibir():
	if query_db("SELECT nome FROM Bar") != []:
		contents = query_db("SELECT * FROM Bar")
	else:
		contents = 'Nao existe nenhum bar cadastrado.'

	return render_template("index.html", contents = contents)
	
@app.route("/<int:id_bar>")
def mostrar(id_bar):	
	contents = query_db("SELECT * FROM Bar WHERE id_bar = ?", id_bar)

	return render_template("bar_detalhe.html", contents = contents)


if __name__ == "__main__":
    #init_db()
    app.run()
