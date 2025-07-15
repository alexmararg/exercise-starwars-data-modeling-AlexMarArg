import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    subscription_date = Column(DateTime)
    
    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    climate = Column(String(120))
    terrain = Column(String(120))
    population = Column(String(50))
    
    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    gender = Column(String(20))
    birth_year = Column(String(20))
    eye_color = Column(String(20))
    
    favorites = relationship('Favorite', back_populates='character')

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    
    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')

def generate_diagram():
    try:
        render_er(Base, 'diagram.png')
        print("¡Diagrama generado correctamente!")
    except Exception as e:
        print("Error generando diagrama:", e)

if __name__ == "__main__":
    generate_diagram()