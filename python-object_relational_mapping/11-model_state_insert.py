#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database"""
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
    addstate = State(name="Louisiana")
    session.add(addstate)
    print(addstate.id)
    session.commit()
    session.close()
