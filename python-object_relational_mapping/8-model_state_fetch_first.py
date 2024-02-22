#!/usr/bin/python3
"""Script that prints the first State object from the database"""
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
    row = session.query(State).first()
    if row is not None:
        print(f"{row.id}: {row.name}")
    else:
        print("Nothing")
    session.close()
