from src import db, login_manager
from sqlalchemy.sql import func
from flask_login import UserMixin

#zapisuję w session zalogowanego usera, jego id
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text())
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    time_finish = db.Column(db.DateTime(timezone=True), default=func.now())
    done = db.Column(db.Boolean, nullable=False, default=False)
    undone = db.Column(db.Boolean, nullable=False, default=False)
    task_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __repr__(self):
        return f"Task('{self.title}')"


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    task = db.relationship('Task', backref='tasks', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)