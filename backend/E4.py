from sqlalchemy .orm import Session 
from datetime import date 
import functions 

def set_recruiting(id, recruiting):
    session = Session(engine)
    club = session.query(Clubs).filter(Clubs.id == id).first()
    response = None
    if club:
        club.recruiting = recruiting
        session.commit()
        response = {
            "id": club.id,
            "name": club.name,
            "category": club.category,
            "seats": club.seats,
            "deadline": club.deadline,
            "recruiting": club.recruiting
        }
    session.close()
    return response