from flask import Blueprint, render_template, request
from datetime import datetime
from flask_login import current_user, login_required
from src import db
from src.models import Task

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # wyświetla zadania pzrypisane do konkretnego usera i sortuję je
    tasks = Task.query.filter_by(task_id = current_user.id).order_by(Task.date_created.desc())

    if request.method == 'POST':
        if request.form.get('done'):
            task_id = request.form.get('form_id')
            field_bool = Task.query.filter_by(id=int(task_id)).first()
            field_bool.done = True
            db.session.commit()

    for time in tasks:
        if time.time_finish < datetime.now():
            time.undone = True
            db.session.commit()

    return render_template('home.html', 
    title='Home', 
    tasks=tasks,
    name=current_user.username
)