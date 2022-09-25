from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Tilte', validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    time_finish = DateTimeField('Time to Finish', format='%Y-%m-%dT%H:%M', validators=[DataRequired()] )
    submit = SubmitField('Add Task')