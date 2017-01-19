from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def query_one():
	puppies = session.query(Puppy).order_by(Puppy.name)
	for puppy in puppies:
		print(puppy.name)

def query_two():
	young_puppies = session.query(Puppy).filter_by()

def query_three():
	puppies = session.query(Puppy).order_by(Puppy.weight)
	for puppy in puppies:
		print(puppy.name, puppy.weight)


#query_one()
query_three()