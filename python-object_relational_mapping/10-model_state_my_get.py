#!/usr/bin/python3
"""Script that prints State object with name passed as arg from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name == sys.argv[4]).first()
    if rows is not None:
        print(rows.id)
    else:
        print("Not found")
