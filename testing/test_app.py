from unittest import TestCase
from urllib import response
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Director, Work
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
        movie1 = Work(movie='Transformers', director_id=1)
        db.session.add(movie1)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class Testhome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

class Testview(TestBase):
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Micheal Bay', response.data)
        self.assertIn(b'Transformers', response.data)

class Testadddirector(TestBase):
    def test_add_director(self):
        response = self.client.post(url_for('add_director'),
        data =dict(director="Micheal Bay"),follow_redirects=True
        )
        self.assertIn(b'Micheal Bay', response.data)

class Testaddwork(TestBase):
    def test_add_work(self):
        response = self.client.post(url_for('add_work'),
        data =dict(movie_name="Transformers", director="Micheal Bay"),follow_redirects=True)
        self.assertIn(b'Transformers', response.data)
        self.assertIn(b'Micheal Bay', response.data)

class Testadddir(TestBase):
    def test_add_dir(self):
        response = self.client.get(url_for('add_director'),
        data =dict(director=""),follow_redirects=True)
        self.assertIn(b'', response.data)

class Testupp(TestBase):
    def test_upp(self):
        response = self.client.get(url_for('update', id=1),
        data =dict(director=""),follow_redirects=True)
        self.assertIn(b'', response.data)

class Testupdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('update', id=1),
        data =dict(director_name="Michael eBay"),follow_redirects=True)
        self.assertIn(b'Michael eBay', response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.post(url_for('delete', id=1))
        self.assertNotIn(b'Micheal eBay', response.data)