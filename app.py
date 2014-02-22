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
		with open ('fileToWrite.txt','w') as fileOutput:
			if request.form.get('nome_bar'):
			    fileOutput.write(request.form.get('nome_bar'))
			    fileOutput.write(' | ')
			if request.form.get('endereco'):
				fileOutput.write(request.form.get('endereco'))
				fileOutput.write(' | ')
			if request.form.get('horario_ini'):
			    fileOutput.write(request.form.get('horario_ini'))
			    fileOutput.write(' | ')
			if request.form.get('horario_fin'):
			    fileOutput.write(request.form.get('horario_fin'))
			    fileOutput.write(' | ')
			if request.form.get('especialidade'):
			    fileOutput.write(request.form.get('especialidade'))
			    fileOutput.write(' | | ')
			else:
				flash('Coloque todas os dados')
		
	return render_template("index.html")


if __name__ == "__main__":
    app.run()