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


