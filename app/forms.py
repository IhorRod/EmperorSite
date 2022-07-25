from flask_wtf import Form
from wtforms import BooleanField, StringField
from wtforms.validators import data_required


class LoginForm(Form):
    openid = StringField('openid', validators=[data_required()])
    remember_me = BooleanField('remember_me', default=False)
