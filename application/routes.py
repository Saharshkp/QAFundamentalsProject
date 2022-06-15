from application import app, db
from application.models import Work, Director
from application.forms import directorForm, workForm
from flask import Flask, render_template, request, url_for, redirect
from requests import post
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm

@app.route('/')
@app.route('/home', methods = ['GET'])
def home():
    message = ''
    return render_template('home.html', message = message)

def pop_dir(j):
    directors = db.session.query(Director).all()
    for i in directors:
        j.director.choices.append((i.id, i.director))

@app.route('/add_movie', methods = ['GET','POST'])
def add_work():
    add = workForm()
    pop_dir(add)
    if request.method == 'POST':
        if add.validate():
            work = Work(
                movie = add.movie_name.data,
                director_id = add.director.data
            )
            db.session.add(work)
            db.session.commit()
            return redirect(url_for('read'))

    return render_template('add.html', add=add)

@app.route('/add_director', methods = ['GET','POST'])
def add_director():
    add_director = directorForm()
    if request.method == 'POST':
                new_dirr = Director(director=add_director.director_name.data)
                db.session.add(new_dirr)
                db.session.commit()
                return redirect(url_for('read'))
                
    return render_template('dir.html', add_director=add_director)

@app.route('/read', methods=['GET'])
def read():
    works = Work.query.all()
    directors = Director.query.all()
        
    return render_template('read.html', works=works, directors=directors)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    director = Director.query.get(id)
    update = directorForm()
    
    if request.method == 'POST':
        director.director= update.director_name.data
        db.session.commit()
        
        return redirect(url_for('read'))

    return render_template('update.html', work=director, update=update)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    director = Director.query.get(id)
    db.session.delete(director)
    db.session.commit()
    return render_template ('read.html', work=Work.query.all())