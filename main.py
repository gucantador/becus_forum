from flask import Flask, render_template, request, flash, redirect, url_for
from forms import FormLogin, FormCriarConta
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
lista_usuarios = ['Gustavo', 'José Carlos']
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# as linhas a seguir criam o banco de dados 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///becus.db'
database = SQLAlchemy(app)
# ----------------------------------------------------------------

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

@app.route("/login", methods=['GET', 'POST'])
def login ():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    #condição para ir para a pagina home depois de fazer login e criar conta

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash('Login feito com sucesso', 'alert-success')  
        return redirect(url_for('home'))    

    if form_login.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash('login feito com sucesso' , 'alert-success')
        return redirect(url_for('home'))  
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
    