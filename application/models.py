from application import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(15))
    Legend_name = db.Column(db.String(15))
    player = db.relationship('Player', backref='team')
    

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_Gk = db.Column(db.String(30))
    player_Def = db.Column(db.String(30))
    player_Mid = db.Column(db.String(30))
    player_Att = db.Column(db.String(30))
    country_id = db.Column(db.integer, db.ForeignKey('team.id'))
    
