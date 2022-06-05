from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators 



class TeamForm(FlaskForm):
    Team_name = StringField('Team Name:', [validators.length(min=1, max=25), validators.DataRequired()])
    Legend_name = SelectField('Choose your Legend', choices = [('ronaldo','Ronaldo'), ('pele','Pele'), ('maradona', 'Maradona'),('figo','Figo'),('nedved', 'Nedved'), ('inzaghi','Inzaghi')])
    submit = SubmitField('Choose')

    def validate_name(self, name):
        name_object = Legend.query.filter_by(Legend_name=Legend_name.data).first()
        if name_object:
            raise ValidationError ("Please choose another Legend")

class PlayerForm(FlaskForm):
    Player