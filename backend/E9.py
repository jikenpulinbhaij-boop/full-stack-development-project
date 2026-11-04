from sqlalchemy.orm import Session
import functions


def get_summary():
    session = Session(functions.engine)

    summary = session.query(functions.Clubs.id, functions.Clubs.name, functions.count(functions.Applications.id)).join(functions.Applications).group_by(functions.Clubs.id).all()

    response = []

    for item in summary:
        temp_summary = {
            "club_id": item[0],
            "club_name": item[1],
            "applications": item[2]
        }
        response.append(temp_summary)

    session.close()
    return response