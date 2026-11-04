from sqlalchemy.orm import Session
import functions

def get_summary():
    session = Session(functions.engine)
    clubs = session.query(functions.Clubs).all()
    response = []

    for club in clubs:
        applications = session.query(functions.Applications).filter(functions.Applications.club_id == club.id).all()
