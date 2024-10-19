from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ManufacturerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    country = StringField('Country', validators=[DataRequired()])
    certificates = StringField('Certificates')
    internal_id = StringField('Internal ID', validators=[DataRequired()])
    submit = SubmitField('Add Manufacturer')
