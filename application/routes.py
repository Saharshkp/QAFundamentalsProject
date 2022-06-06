from application import app, db
from application.models import work

@app.route('/')
@app.route('/home')
def home():
    form = DirectorForm()
    message = ''
    return render_template('home.html', form = form, message = message)

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
    add_director = DirForm()
    if request.method == 'POST':
                new_dirr = Director(dir_name=add_director.dev_name.data)
                db.session.add(new_dirr)
                db.session.commit()
                return redirect(url_for('read'))

    return render_template('dir.html', add_director=add_director)

@app.route('/read', methods=['GET'])
def read():
    work = work.query.all()
    dirr = director.query.all()
    return render_template('read.html', games=game, dir=dirr)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    work = work.query.get(id)
    update = WorkForm()
        
    if request.method == 'POST':
        movie.name = update.movie_name.data
        show.name = update.show_name.data
        work.director_id = update.director.data

        return redirect(url_for('read'))

    return render_template('update.html', work=work, update=update)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    workk = workk.query.get(id)

    db.session.delete(game)
    db.session.commit()
    return render_template ('read.html', workk=workk.query.all())