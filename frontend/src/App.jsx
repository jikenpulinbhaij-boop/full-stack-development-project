import { useState, useEffect } from "react";
import ClubList from "./components/ClubList";
import MyApplications from "./components/MyApplications";
import AddClub from "./components/AddClub";
import ClubItem from "./components/ClubItem";


const API_URL = "http://127.0.0.1:8001";
function App() {
  const [clubs, setClubs] = useState([]);
  const [applications, setApplications] = useState([]);
  const [rollNo, setRollNo] = useState("");

  useEffect(() => {
    fetch(API_URL + "/clubs")
      .then((response) => response.json())
      .then((data) => setClubs(data));
  }, []);

function addClub(name, category, seats, deadline) {
    fetch(API_URL + "/clubs?name=" + name + "&category=" + category + "&seats=" + seats + "&deadline=" + deadline, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, category: category, seats: seats, deadline: deadline }),
    })
      .then(() => fetch(API_URL + "/clubs"))
      .then((response) => response.json())
      .then((data) => setClubs(data)); 
  }


  function toggleRecruitment(id, recruiting) {
    fetch(API_URL + "/clubs/" + id + "/recruitment?recruiting=" + recruiting, { method: "PATCH" })
      .then(() => fetch(API_URL + "/clubs"))
      .then((response) => response.json())
      .then((data) => setClubs(data));
  }


  function apply(id, whyJoin) {
    fetch(API_URL + "/clubs/" + id + "/applications?roll_no=" + rollNo + "&why_join=" + whyJoin, {
    method: "POST"
  })
      .then(() => fetch(API_URL + "/clubs"))
      .then((response) => response.json())
      .then((data) => setClubs(data));
  }


  function showApplications(roll) {
    fetch(API_URL + "/students/" + roll + "/applications")
      .then((response) => response.json())
      .then((data) => setApplications(data));
  }


  function updateStatus(id, status, roll) {
    fetch(API_URL + "/applications/" + id + "/status?status=" + status, { method: "PATCH" })
      .then(() => showApplications(roll));
  }


  function withdrawApplication(id, roll) {
    fetch(API_URL + "/applications/" + id + "/withdraw?roll_no=" + roll, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ roll_no: roll }),
    })
      .then(() => fetch(API_URL + "/students/" + roll + "/applications"))
      .then((response) => response.json())
      .then((data) => setApplications(data)); 
  }

  return (
    <>
      Roll number <input onChange={(e) => setRollNo(e.target.value)} />
      <ClubList clubs={clubs} onApply={apply} onToggle={toggleRecruitment} />
      <MyApplications applications={applications} onShow={showApplications} onStatus={updateStatus} onWithdraw={withdrawApplication} />
      <AddClub onAdd={addClub} />
    </>
  );
}

export default App;
