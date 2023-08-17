from app import db
from app.models import Item
from app import app

if __name__ == "__main__":
    i1 = Item(nome="ps5", preco=4500, cod_barra="8346582", descricao="Console de nova geração")
    i2 = Item(nome="Iphone", preco=10000, cod_barra="32423", descricao="Celular Top")

    with app.app_context():
        db.session.add(i1)
        db.session.add(i2)
        db.session.commit()

    print("Item adicionado com sucesso!")
