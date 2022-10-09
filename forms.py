from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, RadioField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class PetForm(FlaskForm):
    """Form for adding a new pet to adoption website."""

    name = StringField('Pet Name', validators=[InputRequired(message="Name cannot be blank")])
    species = RadioField('Species', choices=[('dog','Dog'), ('cat','Cat'),('porcupine','Porcupine')])
    photo_url = StringField('Photo URL', validators=[URL(message="Must be valid URL"), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0,max=30, message="Must be 0-30")])
    notes = TextAreaField('Notes')

class EditForm(FlaskForm):
    """A form for editing existing pets."""

    photo_url = StringField('Photo URL', validators=[URL(message="Must be valid URL"), Optional()])
    notes = TextAreaField('Notes')
    available = RadioField('Available', choices=[(True,'Yes'),(False,'No')], validators=[Optional()])