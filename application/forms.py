from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators 



class DirectorForm(FlaskForm):
    Director_name = StringField('Add Director ', [validators.length(min=1, max=25), validators.DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        director_object = Director.query.filter_by(Director_name=Director_name.data).first()
        if name_object:
            raise ValidationError ("This Director has already been added.")

class WorkForm(FlaskForm):
    movie_name = StringField('Add Movie ', [validators.length(min=1, max=25), validator.DataRequired()])
    show_name = StringField('Add Show ', [validators.length(min=1, max=25), validator.DataRequired()])
    developer = SelectField ('Who directed this? ', choices=[])
    submit = SubmitField('Add')

    def validate_name(self, name):
        movie_object = movie.query.filter_by(movie_name=movie_name.data).first()
        if movie_object:
            raise ValidationError ("This movie has already been added.")
        show_object = show.query.filter_by(show_name=show_name.data).first()
        if show_object:
            raise ValidationError ("This show has already been added.")