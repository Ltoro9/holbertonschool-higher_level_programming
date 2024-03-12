#!/usr/bin/python3
"""
    script that adds the State object “Louisiana”
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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    rows = session.query(State).where(State.name == "Louisiana").all()

    for row in rows:
        print(f"{row.id}")

    session.close()
