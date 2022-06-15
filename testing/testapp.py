from unittest import TestCase
from urllib import response
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Director, Work, workForm, directorForm
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
            SECERT_KEY='TEST_SECRET_KEY',
            DEBUG=True, 
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Director(director='Micheal Bay')
        db.session.add(sample1)
        db.session.commit()
        movie1 = Work(movie='Transformers')
        db.session.add(movie1)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class Testview(TestBase):
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertIn(b'Micheal Bay', response.data)
        self.assertIn(b'Transformers', response.data)

class Testadddirector(TestBase):
    def test_add_directtor(self):
        response = self.client.post(url_for('add_director'),
        data =dict(game_name="Micheal Bay"),follow_redirects=True
        )
        self.assertIn(b'Micheal Bay', response.data)

class Testaddwork(TestBase):
    def test_add_work(self):
        response = self.client.post(url_for('add'),
        data =dict(dev_name="Transformers"),follow_redirects=True
        )
        self.assertIn(b'Transformers', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.post(url_for('delete', id=1))
        self.assertNotIn(b'Micheal Bay', response.data)
        self.assertNotIn(b'Bethesda', response.data)

class Testupdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('update', id=1),
        data =dict(Director_name="Duffer Brothers"),follow_redirects=True
        )
        self.assertIn(b'Duffer Brothers', response.data)
