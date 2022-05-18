from main import database
from datetime import datetime

# esse arquivo cria as colunas do banco de dados
database.metadata.clear()
class Usuario(database.Model):  # o nome da classe 'usuario' por exemplo, quem decide somos nos, o atributo vem do flask, cada variavel é uma coluna que a gente pode criar 
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    empresa = database.Column(database.String)
    funcao = database.Column(database.String)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy = True)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criancao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

