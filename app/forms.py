from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class AddPropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[InputRequired(), NumberRange(min=1, max=10)])
    bathrooms = IntegerField('Bathrooms', validators=[InputRequired(), NumberRange(min=1, max=10)])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[InputRequired(), NumberRange(min=0)])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description')
    photo = FileField('Photo', validators=[DataRequired()])
