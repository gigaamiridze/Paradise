from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, RadioField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class Signup(FlaskForm):
    role = RadioField(choices=[('artist', 'Artist'), ('listener', 'Listener')], validators=[DataRequired()])
    username = StringField(validators=[DataRequired(), Length(4, 25)])
    name = StringField(validators=[DataRequired(), Length(4, 20)])
    email = EmailField(validators=[DataRequired(), Email(), Length(10, 30)])
    password = PasswordField(validators=[DataRequired(), Length(8, 25),
                                         EqualTo('conf_pass', message='Passwords must much')]
                             )
    conf_pass = PasswordField(validators=[DataRequired()])
    birth_date = DateField(validators=[DataRequired()])
    gender = RadioField(choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('sign up now')

class Signin(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField()
    submit = SubmitField('sign in now')