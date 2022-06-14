from application import db
from flask import Flask, render_template, request, url_for, redirect
import os
from sqlalchemy import Integer
from flask_sqlalchemy import SQLAlchemy


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    director = db.Column(db.String(20))
    work = db.relationship('Work', backref='director')

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(30))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
