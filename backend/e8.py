from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

DB_PATH = "clubs.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

# Endpoint 1
def get_all_students():
    with Session(engine) as session: 
        students = session.query(Students).all()
        return [_students_to_dict(student) for student in students]


