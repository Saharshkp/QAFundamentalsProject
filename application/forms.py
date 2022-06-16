from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Length, ValidationError

class directorForm(FlaskForm):
    director_name = StringField('Director: ', [validators.length(min=1, max=25), validators.DataRequired()])
    submit = SubmitField('Add')
    

class workForm(FlaskForm):
    movie_name = StringField('New Movie ', [validators.length(min=1, max=25), validators.DataRequired()])
    director = SelectField('Who directed this? ', choices=[])
    submit = SubmitField('Add')

            
