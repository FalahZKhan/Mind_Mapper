from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MindMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
