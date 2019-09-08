from flask import Flask
from dotenv import load_dotenv
#from pathlib import Path
import os
from app.models import *

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

#Object of Flask class
app = Flask(__name__)

#Explicitly providing path to '.env' to access data from there.
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path=env_path)

#importing config.py app setting information
app.config.from_object(os.getenv('app_settings'))


# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
# Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# class ScrappedHotels(db.Model):
#     __tablename__ = 'scrapped_hotels'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), index=True)
#     hotel_unique_id = db.Column(db.String(255), index=True)
#     address = db.Column(db.String(255))


