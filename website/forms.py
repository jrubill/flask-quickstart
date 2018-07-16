from flask_wtf import FlaskForm 
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LogInForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
