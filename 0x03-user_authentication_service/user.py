#!/usr/bin/env python3
'''SQLAlchemy model named User for a database table named users'''


import sqlalchemy
from sqlalachemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    '''user class inheriting from declarative base'''
    __tablename__ = users
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
