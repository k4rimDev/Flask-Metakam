from flask_wtf import FlaskForm

from wtforms import StringField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class BrandForm(FlaskForm):
    logo = FileField('Logo')
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    internal_id = StringField('Internal ID', validators=[DataRequired()])
    submit = SubmitField('Add Brand')