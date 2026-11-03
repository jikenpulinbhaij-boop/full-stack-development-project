# write your main.py code here
from fastapi import FastAPI
import functions

app = FastAPI()

@app.get("/clubs")
def clubs():
    return functions.get_all_clubs()

@app.get("/clubs/{id}")
def club(id):
    return functions.get_club(id)

@app.post("/clubs")
def add_club(name, description, contact, location = None):
    return functions.add_club(name=name, description=description,contact =contact,location=location)

@app.patch("/clubs/{id}/recruitment")
def update_club(id, name=None, description=None, contact=None, location=None):
    return functions.update_club(id=id, name=name, description=description, contact=contact, location=location)

@app.post("/clubs/{club_id}/applications")
def add_student(name, email, contact, club_id):
    return functions.add_student(name=name, email=email, contact=contact, club_id=club_id)

@app.patch("/applications/{application_id}/status")
def update_student_status(application_id, status):
    return functions.update_student_status(application_id=application_id, status=status)

@app.patch("/applications/{application_id}/withdraw")
def withdraw_application(application_id):
    return functions.withdraw_application(application_id=application_id)

@app.get("/students/{roll_no}/applications")
def get_student_applications(roll_no):
    return functions.get_student_applications(roll_no=roll_no)

@app.get("/clubs/summery")
def get_club_summary():
    return functions.get_club_summary()

