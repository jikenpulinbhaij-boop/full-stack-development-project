from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import date
import functions

def get_summary():
    session = Session(functions.engine)
    clubs = session.query(functions.Clubs).all()
    response = []

    for club in clubs:
        applications = session.query(functions.Applications).filter(
            functions.Applications.club_id == club.id
        ).all()

        response.append({
            "club_id": club.id,
            "club_name": club.name,
            "applied": len([a for a in applications if a.status == "applied"]),
            "shortlisted": len([a for a in applications if a.status == "shortlisted"]),
            "selected": len([a for a in applications if a.status == "selected"]),
            "rejected": len([a for a in applications if a.status == "rejected"])
        })

    session.close()
    return response