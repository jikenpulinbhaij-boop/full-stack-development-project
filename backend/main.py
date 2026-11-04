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