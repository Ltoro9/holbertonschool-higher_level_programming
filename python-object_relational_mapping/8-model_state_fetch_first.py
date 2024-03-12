#!/usr/bin/python3
"""
    script that prints the first State object
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

    rows = session.query(State).order_by(State.id).first()

    print(f"{rows.id}: {rows.name}")

    session.close()
