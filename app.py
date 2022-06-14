from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from application import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

db = SQLAlchemy(app)

from application import routes
