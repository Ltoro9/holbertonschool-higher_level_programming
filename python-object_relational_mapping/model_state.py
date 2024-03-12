#!/usr/bin/python3
"""
    python file that contains the class definition of a State and an instance
    Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()


class State(Base):
    """
        Represents a state entity in the database.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
