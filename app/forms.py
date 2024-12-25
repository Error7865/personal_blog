from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    email=EmailField(name='email',validators=[DataRequired()])
    password=PasswordField(name='password',validators=[DataRequired()])
    cpassword=PasswordField(name='confirm', validators=[DataRequired()])

class Login(FlaskForm):
    username=StringField(name='username', validators=[DataRequired()])
    password=PasswordField(name='password',validators=[DataRequired()])

class ArticleForm(FlaskForm):
    hide=HiddenField(name='hide')
    title=StringField(name='title', validators=[DataRequired()])
    textarea=TextAreaField(name='desc', validators=[DataRequired()])