#!/usr/bin/python3
"""Script that lists all State objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        f'mysql://{username}:{password}@localhost/hbtn_0e_0_usa')
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        print(row.id, row.name)
    session.close()
