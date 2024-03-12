#!/usr/bin/python3
"""
    script that lists all State objects that contain the letter 'a'
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db_url = (f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{database}")
    engine = create_engine(db_url)

    session = sessionmaker(bind=engine)
    session = session()

    rows = session.query(State).order_by(State.id)\
        .where(State.name.like('%a%')).all()

    for row in rows:
        print(f"{row.id}: {row.name}")

    session.close()
