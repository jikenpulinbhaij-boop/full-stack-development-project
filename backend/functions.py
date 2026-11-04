from sqlalchemy import Integer, String, Column, create_engine , ForeignKey
from sqlalchemy.orm import declarative_base

DB_PATH = "recruitment.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

class Clubs(Base):
    __tablename__ = "clubs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    seats = Column(Integer)
    deadline = Column(String)
    recruiting = Column(Integer)


class Applications(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    club_id = Column(Integer,ForeignKey("clubs.id"))
    roll_no = Column(Integer)
    why_join = Column(String)
    status = Column(String)
    applied_on = Column(String)

Base.metadata.create_all(engine)