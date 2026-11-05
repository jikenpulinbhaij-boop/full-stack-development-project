from sqlalchemy import func
from sqlalchemy.orm import Session
import functions


def get_summary():
    session = Session(functions.engine)

    summary = session.query(functions.Clubs.name, functions.Applications.status, func.count(functions.Applications.id)).join(functions.Applications).group_by(functions.Clubs.name, functions.Applications.status).all()

    response = []

    for item in summary:
        temp_summary = {
            "club_name": item[0],
            "status": item[1],
            "count": item[2]
        }
        response.append(temp_summary)

    session.close()
    return response