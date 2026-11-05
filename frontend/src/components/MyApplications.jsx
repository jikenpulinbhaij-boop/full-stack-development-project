import { useState } from "react";

function MyApplications({ applications, onShow, onStatus, onWithdraw }) {
  const [rollNo, setRollNo] = useState("");

  return (
    <>
      <h1>My applications</h1>
      <input placeholder="Your roll number" value={rollNo} onChange={(e) => setRollNo(e.target.value)} />
      <button onClick={() => onShow(rollNo)}>Show</button>
      <ul>
        {applications.map((application) => (
          <li key={application.id}>
            Club {application.club_id} · {application.status}
            <select value={application.status} onChange={(e) => onStatus(application.id, e.target.value, rollNo)}>
              {["applied", "shortlisted", "selected", "rejected", "withdrawn"].map((s) => <option key={s}>{s}</option>)}
            </select>
                        {application.status === "applied" ? (
              <button onClick={() => onWithdraw(application.id, rollNo)}>Withdraw</button>
            ) : null}
          </li>
        ))}
      </ul>
    </>
  );
}

export default MyApplications;
