#!/usr/bin/python3
"""
    write a script 14-model_city_fetch_by_state.py
    that prints all City objects
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State


if __name__ == "__main__":

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db_url = (f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{database}")
    engine = create_engine(db_url)

    session = sessionmaker(bind=engine)
    session = session()

    rows = session.query(City, State)\
        .join(State, City.state_id == State.id).all()

    for city, state in rows:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
