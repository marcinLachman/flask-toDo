from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from src import db
from src.models import Users
from src.users.forms import RegisterForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            flash('This name exist in our database', 'error')
        else:
            hash_password = generate_password_hash(form.password.data, method='sha256')
            new_user = Users(
                username = form.username.data,
                password = hash_password,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("User created!", 'success')
            return redirect(url_for('main.home'))

    return render_template('users/register.html', 
    title='Register Page',
    form=form,
)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You Are Logged', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Wrong password or username', 'error')

    return render_template('users/login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))