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

@app.route('/add', methods = ['GET','POST'])
def add_work():
    add = workForm()
    if request.method == 'POST':
        if add.validate():
            work = Work(
                name = add.work_name.data,
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

@app.route('/read', methods=['GET', 'POST'])
def read():
    # movies = Work.query.all()
    # directors = Director.query.all()
    form = directorForm
    dirr = Director.query.join(Work).all()
    workk = db.session.query(Work).all()
    for i in workk:
        form.director_name.choices.append((i.id.i.director_name))
        
    return render_template('read.html', work=Work, director=Director)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    work = Work.query.get(id)
    update = WorkForm()
        
    if request.method == 'POST':
        movie.name = update.movie_name.data
        work.director_id = update.director.data

        return redirect(url_for('read'))

    return render_template('update.html', work=Work, update=update)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    work = Work.query.get(id)

    db.session.delete(work)
    db.session.commit()
    return render_template ('read.html', work=Work.query.all())