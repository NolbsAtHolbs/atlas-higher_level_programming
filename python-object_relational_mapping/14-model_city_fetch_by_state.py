#!/usr/bin/python3
"""Script that prints all City objects from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    allcities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for city, state in allcities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()
