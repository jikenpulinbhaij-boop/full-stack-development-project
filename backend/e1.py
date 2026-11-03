from sqlalchemy.orm import Session, session
import functions
from daytime import datetime

DB_PATH = "recruitment.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
session = Session(engine)

def get_clubs():
    return session.query(functions.Clubs).all()

def get_clubs(club_id):
    return session.query(functions.Clubs).filter(functions.Clubs.id == club_id).first()

def get_student_applications(roll_no):
    return session.query(functions.Applications).filter(functions.Applications.roll_no == roll_no).all()    
