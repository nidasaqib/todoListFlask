from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 

# file_path = os.path.abspath(os.getcwd())+"/todo.db"

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import routes 
