from app import db
from app import app
from app.models import User, Item

with app.app_context():
    item2 = Item.query.get(2)  # Ajuste o número 2 para o ID do item que você deseja atualizar
    user = User.query.filter_by(usuario='fulano').first()

    if user:
        item2.dono = user.id
        db.session.commit()
    else:
        print("Usuário não encontrado.")
