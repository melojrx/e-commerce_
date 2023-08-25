from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import User

class CadastroForm(FlaskForm):

    usuario = StringField(label='Usuário:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha:', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')

    def validate_usuario(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário.")
    
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro e-mail.")
    
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe! Cadastre outra senha")
        
class LoginForm(FlaskForm):
    usuario = StringField(label='Usuário:', validators=[DataRequired()])
    senha = PasswordField(label='Senha:', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')

class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label='Comprar produto!')

class VendaProdutoForm(FlaskForm):
    submit = SubmitField(label='Vender produto!')