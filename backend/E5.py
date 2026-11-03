from sqlalchemy.orm import Session 
from datetime import date
import functions

def add_club(name, category, seats, deadline):
    session = Session(engine)
    club = Clubs(name=name, category=category, seats=seats, deadline=deadline, recruiting=recruiting)
    session.add(club)
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



