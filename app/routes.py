from flask import render_template, redirect, url_for, flash
from app import app 
from app.models import Item, User
from app.forms import CadastroForm, LoginForm, CompraProdutosForm
from app import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
def page_home():
        return render_template('home.html')
    
@app.route('/produtos', methods=['GET', 'POST'])
@login_required
def page_produtos():
      compra_form = CompraProdutosForm()
      itens = Item.query.all()
      return render_template('produtos.html', itens=itens, compra_form=compra_form)

@app.route('/login', methods=['GET', 'POST'])
def page_login():
      form = LoginForm()
      if form.validate_on_submit():
            usuario_logado = User.query.filter_by(usuario=form.usuario.data).first()
            if usuario_logado and usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
                  login_user(usuario_logado)
                  flash(f'Logado com Sucesso! Seu login é {usuario_logado.usuario}.', category='success')
                  return redirect(url_for('page_produtos'))
            else:
                  flash(f'Usuário ou senha inválidos! Tente Novamente!', category='danger')
      return render_template('login.html', form=form)


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
      form = CadastroForm()
      if form.validate_on_submit():
            usuario = User(
                  usuario = form.usuario.data, 
                  email = form.email.data, 
                  senhacrip = form.senha1.data
                )
            db.session.add(usuario)
            db.session.commit()

            flash(f'Cadastro efetuado com sucesso!', category='success')
            return redirect(url_for('page_produtos'))
      
      
      if form.errors.values():
            for error in form.errors.items():
                  flash(f' Erro ao Cadastrar usuário: {error}', category='danger')
            
      return render_template('cadastro.html', form=form)

@app.route('/logout')
def page_logout():
      logout_user()
      flash(f'Logout efetuado com sucesso!', category='info')
      return redirect(url_for('page_home'))