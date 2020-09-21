from flask_wtf import FlaskForm
from wtform import StringField,PasswordField,SubmitField,BooleanField
from wtform.validators import DataRequired,Length,Email,EqualTo



class RegistrationForm(FlaskForm):
	username = StringField('Username')
	email = StringField('Email')
	password= PasswordField('Password')
	confirm_password= PasswordField('confirm Password',EqualTo('password'))
	submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
	
	email = StringField('Email')
	password= PasswordField('Password')
	remember=BooleanField('Remember Me')
	submit=SubmitField('Sign Up')