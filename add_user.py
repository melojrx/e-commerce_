from app import db
from app.models import User
from app import app

if __name__ == "__main__":
    user1 = User(usuario="melojr", email='eu@mail.com', senha="il5369", valor=10000)
    

    with app.app_context():
        db.session.add(user1)
        db.session.commit()

    print("user adicionado com sucesso!")