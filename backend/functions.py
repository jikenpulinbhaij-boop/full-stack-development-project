from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.orm import declarative_base

DB_PATH = "recruitment.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

class Clubs(Base):
    __tablename__ = "clubs"

    id = Column[int](Integer, primary_key=True)
    name = Column[str](String)
    category = Column[str](String)
    seats = Column[int](Integer)
    deadline = Column[str](String)
    recruiting = Column[int](Integer)


class Applications(Base):
    __tablename__ = "applications"

    id = Column[int](Integer, primary_key=True)
    club_id = Column[int](Integer)
    roll_no = Column[str](String)
    why_join = Column[str](String)
    status = Column[str](String)
    applied_on = Column[str](String)

Base.metadata.create_all(engine)

