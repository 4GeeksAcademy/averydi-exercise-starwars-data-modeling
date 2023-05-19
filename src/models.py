import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key = True)
    name = Column(String(250),nullable = False)
    model = Column(String(250),nullable = False)
    manufacturer = Column(String(250),nullable = False)
    cost_in_credits = Column(String(250),nullable = False)
    passengers = Column(String(250),nullable = False)
    length = Column(String(250), nullable= False)
    crew = Column(String(250), nullable= False)
    cargo_capacity = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    name = Column(String(250),nullable = False)
    rotation_period = Column(String(250),nullable = False)
    orbital_period = Column(String(250),nullable = False)
    diameter = Column(String(250))
    climate = Column(String(250),nullable = False)
    gravity = Column(String(250),nullable = False)
    terrain = Column(String(250),nullable = False)
    surface_water = Column(String(250),nullable = False)
    population = Column(String(250),nullable = False)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key = True)
    title = Column(String(250),nullable = False)
    episode_id = Column(String(250))
    opening_crawl = Column(String(250),nullable = False)
    director = Column(String(250),nullable = False)
    producer = Column(String(250),nullable = False)
    release_date = Column(String(250),nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    films_id = Column(Integer, ForeignKey('films.id'))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
