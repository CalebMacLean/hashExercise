# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email
# Forms
class RegisterForm(FlaskForm):
    """Form for registering a new user"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First_Name", validators=[InputRequired()])
    last_name = StringField("Last_Name", validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form for logging in a user"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    """Form for creating a feedback instance"""
    title = StringField("Title", validators=[InputRequired()])
    content = StringField("Content", validators=[InputRequired()])

class DeleteForm(FlaskForm):
    """Form is intentionally left blank?"""