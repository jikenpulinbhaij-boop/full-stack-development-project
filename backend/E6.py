from sqlalchemy.orm import Session
import functions

def update_application_status(application_id, status):
    session = Session(functions.engine)

    application = session.query(functions.Applications).filter(functions.Applications.id == application_id).first()

    application.status = status

    response = {
        "id": application.id,
        "club_id": application.club_id,
        "roll_no": application.roll_no,
        "why_join": application.why_join,
        "status": application.status,
        "applied_on": application.applied_on
    }

    session.commit()
    session.close()

    return response