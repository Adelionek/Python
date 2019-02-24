from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
<<<<<<< HEAD
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sing in')


=======
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
>>>>>>> 5efb728e2407126287cba4dc0e4a6198b233dbcb
