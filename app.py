import cgi
from flask import (
		Flask, render_template, flash,
		url_for, redirect, request
)


app = Flask(__name__)
app.config.update({
	'SECRET_KEY': 'Evolux <3 Python',
	'DEBUG': True
})


@app.route("/", methods=['GET', 'POST'])
def bar():
	if request.method == 'POST':
		form = cgi.FieldStorage()
		with open ('lista_bares.yml','a') as fileOutput:
			if '' not in request.form.values():
				dados = ''
				for campo in request.form.values():
					dados += campo + '\n'
				fileOutput.write(dados)
				fileOutput.write('\n---\n')
			else:
				flash('Coloque todos os dados')
		
	return render_template("index.html")

@app.route("/lista")
def exibir():
	f = open('lista_bares.yml', 'r')
	contents = f.read()
	f.close()
	return render_template("lista.html", contents = contents)
	


if __name__ == "__main__":
    app.run()
