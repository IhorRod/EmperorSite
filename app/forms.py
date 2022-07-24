from flask_wtf import Form
from wtforms import BooleanField, TextAreaField
from wtforms.validators import data_required


class LoginForm(Form):
    openid = TextAreaField('openid', validators=[data_required()])
    remember_me = BooleanField('remember_me', default=False)
