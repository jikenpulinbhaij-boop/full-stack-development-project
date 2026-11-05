# Club Recruitment

## Problem Statement

A new academic year brings new faces, fresh ambitions, and countless opportunities. But with dozens of clubs competing for attention and hundreds of students eager to join, where does the excitement end and the chaos begin?

The coder searches for a tech club, the dancer dreams of the stage, and the athlete looks for their team. Yet, between scattered announcements, missed deadlines, duplicate applications, limited seats, and endless follow-ups, finding the right club becomes harder than it should be.

While students are left wondering, "Did I get selected?", coordinators are buried in applications, struggling to track candidates and manage fair selections.
A campus full of connections shouldn't have a recruitment process full of confusion.

The challenge is simple: How can we bring every club, every applicant, and every opportunity under one roof, making recruitment transparent, organized, and fair?


## 1. Who is doing what

Update your own row at every check-in.

| Day | Partner | What are you doing? |
|---|---|---|
| Day 1 | Jiken Pulinbhai Jasoliya | Doing the first 3 Endpoints (endpoints: 1, 2, 8) |
| Day 1 | Abhishek.N | doing endpoints 4, 9  |
| Day 1 | Thanuja | Doing 3rd and 7th end points |
| Day 1 | Sanghavi |working on clubs table, 5th and 6th endpoints  |
| Day 2 | Thanuja |Testing the Backend and debugging  |
| Day 2 | Sanghavi | working on main.py  |
| Day 2 | Jiken | Starting on the frontend  |
| Day 2 | Abhishek |Starting on the Frontend  |
| Day 3 | Thanuja | Debuggin backend, updating the endpoints |
| Day 3 | Sanghavi | Debuggin backend, updating the endpoints  |
| Day 3 | Jiken | adding the more to the frontend, updating the endpoints   |
| Day 3 | Abhishek |updating E9.py, working on frontend   |

## 2. Endpoint tracker

Fill in the method and path from your PRD's endpoint table. 

| # | Method  | path | Request Body | Success Code | Error Codes |
|---|---|---|---|---|---|
| E1 | GET | /clubs |  |  |  |
| E2 | GET | /clubs/{clubs.id} | /{clubs.id} |  |  |
| E3 |post  | /clubs |name , category ,seats,deadline  |  |  |
| E4 | PATCH  | clubs/{club_id}/recruiting  | recruiting  |  |  |
| E5 | POST | /clubs/{club_id}/applications | roll_no, why_join |  |  |
| E6 | PATCH | /applications/{application_id}/status | status | |  |
| E7 |patch |/applications/{applications_id}/withdraw |roll_no |  |  |
| E8 | GET | /students | /{roll_no}/applications |  |  |
| E9 | GET |  /summary |NONE  |  |  |

### flow of the Project Presentation 

->	Problem statement 
->	Distribution of work 
->	API contracts 
->	Frontend Demo 
->	Swagger 
->	File structure 
->	Conclusion 
->	Interesting findings
->	QNA

