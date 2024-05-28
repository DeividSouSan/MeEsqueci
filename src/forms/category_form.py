from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CategoryForm(FlaskForm):
    # TODO: inserir os validators.
    name = StringField("Nome")
