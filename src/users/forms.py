from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=2, max=120)
        ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        Length(min=2, max=120),
        EqualTo('password')
        ])
    submit = SubmitField('Add User')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=50)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=2, max=120)
        ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')