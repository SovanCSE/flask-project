from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask

from sqlalchemy.orm import sessionmaker
# from app import app

engine = create_engine('mysql://root:welcome@localhost/practicedb', echo=True)
#way 1
Base = declarative_base()
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    password = Column(String(255))

    def __repr__(self):

        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                        self.name, self.fullname, self.password)

class Name(Base):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    password = Column(String(255))

    def __repr__(self):

        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                        self.name, self.fullname, self.password)
def create_basedb():
    return Base.metadata.create_all(engine)

#way 2
metadata = MetaData(bind=engine)
user = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
    Column('nickname', String(50), nullable=False)
)
user_prefs = Table('user_prefs', metadata,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

def create_metadatadb():
    return metadata.create_all()

#way3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:welcome@localhost/practicedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class ScrappedHotels(db.Model):
    __tablename__ = 'scrapped_hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    hotel_unique_id = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255))

def create_flaskdb():
    return db.create_all()



