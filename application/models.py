from application import db
from flask import Flask, render_template, request, url_for, redirect
import os
from sqlalchemy import Integer
from flask_sqlalchemy import SQLAlchemy
from  wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_wtf import FlaskForm

class director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director_name = db.Column(db.String(20))
    Work = db.relationship('work', backref='director')
    

class work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(30))
    show = db.Column(db.String(20))
    director_id = db.Column(db.integer, db.ForeignKey('director.id'))
    
