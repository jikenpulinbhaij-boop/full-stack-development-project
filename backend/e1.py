from sqlalchemy.orm import Session
import functions

def get_clubs():
    session = Session(engine)
    clubs = session.query(functions.Clubs).all()
    response = []
    for club in clubs:
        temp_club = {
            "id": club.id,
            "name": club.name,
            "description": club.description,
            "contact": club.contact,
            "location": club.location,
            "resolved_at": club.resolved_at,
            "status": club.status
        }
        response.append(temp_club)
    session.close()
    return response

def get_clubs(club_id):
    session = Session(engine)
    club = session.query(functions.Clubs).filter(functions.Clubs.id == club_id).first()
    
    response = None
    if club:
        response = {
            "id": club.id,
            "name": club.name,
            "description": club.description,
            "contact": club.contact,
            "location": club.location,
            "resolved_at": club.resolved_at,
            "status": club.status
        }
        
    session.close()
    return response

def get_student_applications(roll_no):
    session = Session(engine)
    applications = session.query(functions.Applications).filter(functions.Applications.roll_no == roll_no).all()
    response = []
    for application in applications:
        temp_application = {
            "id": application.id,
            "roll_no": application.roll_no,
            "club_id": application.club_id,
            "status": application.status
        }
        response.append(temp_application)
    session.close()
    return response
