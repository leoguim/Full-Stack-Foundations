import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    city = Column(String(50))
    state = Column(String(100))
    zipCode = Column(String(10))
    website = Column(String)

class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    dateOfBirth = Column(Date)
    gender = Column(String(6), nullable=False)
    weight = Column(Numeric(10))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
        picture = Column(String)

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
