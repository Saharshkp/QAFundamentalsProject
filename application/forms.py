from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Length, ValidationError

class directorForm(FlaskForm):
    director_name = StringField('Director: ', [validators.length(min=1, max=25), validators.DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        director_object = Director.query.filter_by(Director=director.data).first()
        if name_object:
            raise ValidationError ("This Director has already been added.")

class workForm(FlaskForm):
    movie_name = StringField('New Movie ', [validators.length(min=1, max=25), validators.DataRequired()])
    director = SelectField('Who directed this? ', choices=[])
    submit = SubmitField('Add')
    
    def validate_name(self, name):
        movie_object = movie.query.filter_by(movie_name=movie_name.data).first()
        if movie_object:
            raise ValidationError ("This movie has already been added.")
            
