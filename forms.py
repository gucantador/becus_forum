from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    empresa = StringField('Empresa', validators=[DataRequired()])
    funcao = StringField('Função', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('Senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')
 


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_submit_login = SubmitField('Fazer Login')
    lembrar_dados = BooleanField('Lembrar dados de acesso')

# def login():
    # criar = FormCriarConta()
    # login_now = FormLogin()
    # return criar, login_now
    

