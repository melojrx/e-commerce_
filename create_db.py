from app.models import db
from app import app

if __name__ == "__main__":
    app.app_context().push()
    db.drop_all()
    db.create_all()