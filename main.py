from flask import Flask, render_template
import forms
import os



app = Flask(__name__)
lista_usuarios = ['Gustavo', 'José Carlos']
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/projetando")
def projetando():
    return render_template('projetando.html')

@app.route("/dimensionamento")
def dimensionamento():
    return render_template('dimensionamento.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)


@app.route("/forum")
def forum():
    return render_template('forum.html')

@app.route("/login")
def login ():
    return render_template('login.html', code = forms.FormCriarConta.username)


if __name__ == '__main__':
    app.run(debug=True)
    