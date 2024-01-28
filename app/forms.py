from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired
from app.models import list_table


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class TrackerForm(FlaskForm):
    # name = SelectField('name', choices=list_table(), validators=[DataRequired()])
    name = SelectField('name', coerce=int, validate_choice=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[DataRequired()])
    push_ups = IntegerField('Push Ups', validators=[DataRequired()])
    sit_ups = IntegerField('Sit Ups', validators=[DataRequired()])
    pull_ups = IntegerField('Pull Ups', validators=[DataRequired()])
    miles_ran = FloatField('Miles Ran', validators=[DataRequired()])
    submit = SubmitField('Submit Data')
