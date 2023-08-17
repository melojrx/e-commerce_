from app import db, login_manager 
from app import bcrypt  
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    senha = db.Column(db.String(length=60), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)

    @property
    def senhacrip(self):
        return self.senhacrip
    
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    preco = db.Column(db.Float, nullable=False)
    cod_barra = db.Column(db.String(12), nullable=False, unique=True)
    descricao = db.Column(db.String(1024), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f"Item {self.nome}"