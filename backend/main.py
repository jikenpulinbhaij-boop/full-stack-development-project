from fastapi import FastAPI, HTTPException
import E1_2_8
import E3
import E4
import E5
import E6
import E7
import E9

app = FastAPI()

@app.get("/clubs")
def clubs(category=None):

    if category:
        if category not in ["technical", "cultural", "sports", "social", "literary"]:
            raise HTTPException(status_code=422, detail="Invalid category")

    return E1_2_8.get_all_clubs(category=category)

@app.get("/clubs/{club_id}")
def club(club_id: int):

    response = E1_2_8.get_club(id=club_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Club not found")

    return response

@app.post("/clubs")
def add_club(name, category, seats: int, deadline):

    if name == "" or category == "" or deadline == "":
        raise HTTPException(status_code=422, detail="Fields cannot be empty")

    if category not in ["technical", "cultural", "sports", "social", "literary"]:
        raise HTTPException(status_code=422, detail="Invalid category")

    if seats < 1 or seats > 30:
        raise HTTPException(status_code=422, detail="Seats must be between 1 and 30")

    return E3.add_club(name=name, category=category, seats=seats, deadline=deadline)

@app.patch("/clubs/{club_id}/recruitment")
def recruitment(club_id: int, recruiting: bool):

    response = E4.set_recruiting(id=club_id, recruiting=recruiting)

    if response is None:
        raise HTTPException(status_code=404, detail="Club not found")

    return response

@app.post("/clubs/{club_id}/applications")
def apply(club_id: int, roll_no, why_join):

    club = E1_2_8.get_club(id=club_id)

    if club is None:
        raise HTTPException(status_code=404, detail="Club not found")

    if roll_no == "" or why_join == "":
        raise HTTPException(status_code=422, detail="Fields cannot be empty")

    if len(why_join) < 20:
        raise HTTPException(status_code=422, detail="Reason must be at least 20 characters")

    if club["recruiting"] == 0:
        raise HTTPException(status_code=400, detail="Recruitment is closed")

    applications = E1_2_8.get_student_applications(roll_no=roll_no)

    for application in applications:
        if application["club_id"] == club_id:

            if application["status"] == "applied":
                raise HTTPException(status_code=400, detail="Already applied to this club")

            if application["status"] == "shortlisted":
                raise HTTPException(status_code=400, detail="Already applied to this club")

            if application["status"] == "selected":
                raise HTTPException(status_code=400, detail="Already applied to this club")

            if application["status"] == "rejected":
                raise HTTPException(status_code=400, detail="Already applied to this club")

    active_applications = E5.get_active_application_count(roll_no=roll_no)

    if active_applications >= 3:
        raise HTTPException(status_code=400, detail="Maximum 3 active applications allowed")

    return E5.apply_to_club(club_id=club_id, roll_no=roll_no, why_join=why_join)


@app.patch("/applications/{application_id}/status")
def update_status(application_id: int, status):

    application = E7.get_application(id=application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    if application["status"] == "selected" or application["status"] == "rejected" or application["status"] == "withdrawn":
        raise HTTPException(status_code=400, detail="This application cannot be changed")

    if application["status"] == "applied" and status == "selected":
        raise HTTPException(status_code=400, detail="Application must be shortlisted first")

    if status == "selected":

        club = E1_2_8.get_club(id=application["club_id"])

        selected_applications = E6.get_selected_count(club_id=application["club_id"])

        if selected_applications >= club["seats"]:
            raise HTTPException(status_code=400, detail="This club has already filled all its seats.")

        student_selected = E6.get_student_selected_count(roll_no=application["roll_no"])

        if student_selected >= 2:
            raise HTTPException(status_code=400, detail="Student is already selected by 2 clubs")

    return E6.update_application_status(application_id=application_id, status=status)


@app.patch("/applications/{application_id}/withdraw")
def withdraw(application_id: int, roll_no: int):

    application = E7.get_application(id=application_id)

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    if application["roll_no"] != roll_no:
        raise HTTPException(status_code=403, detail="This is not your application")

    if application["status"] != "applied":
        raise HTTPException(status_code=400, detail="Only applied applications can be withdrawn")

    return E7.withdraw_application(id=application_id)


@app.get("/students/{roll_no}/applications")
def student_applications(roll_no: int):

    return E1_2_8.get_student_applications(roll_no=roll_no)


@app.get("/summary")
def summary():

    return E9.get_summary()






