from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from src import db
from src.models import Task
from src.tasks.forms import TaskForm

tasks = Blueprint('tasks', __name__)

@tasks.route('/add-task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()

    if form.validate_on_submit():
        #dodaje zadanie do konkretnego user, foreignkey
        tasker = current_user.id

        task = Task(
            title = form.title.data,
            content = form.content.data,
            time_finish = form.time_finish.data,
            task_id = tasker
        )
        db.session.add(task)
        db.session.commit()
        flash('Task Created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('add-task.html', form=form)