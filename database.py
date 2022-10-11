from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_database(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return db
