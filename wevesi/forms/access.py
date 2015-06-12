from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])


class SignupForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_verify = PasswordField('Verify Password',
                                  validators=[DataRequired()])

