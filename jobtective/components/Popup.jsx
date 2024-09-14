import React, { useState } from 'react';
import './Popup.css';

const Popup = ({ job, closePopup, onJobUpdate }) => {
  const [company, setCompany] = useState(job ? job.company : '');
  const [position, setPosition] = useState(job ? job.position : '');
  const [resume, setResume] = useState(job ? job.resume : '');
  const [date, setDate] = useState(job ? job.date : '');
  const [status, setStatus] = useState(job ? job.status : '');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const updatedJob = { ...job, company, position, resume, date, status };
    onJobUpdate(updatedJob);
    closePopup();
  };

  return (
    <div className="popup">
      <form onSubmit={handleSubmit}>
        <label>
          Company:
          <input type="text" value={company} onChange={(e) => setCompany(e.target.value)} />
        </label>
        <label>
          Position: 
          <input type="text" value={position} onChange={(e) => setPosition(e.target.value)} />
        </label>
        <label>
          Resume: 
          <input type="text" value={resume} onChange={(e) => setResume(e.target.value)} />
        </label>
        <label>
          Date: 
          <input type="text" value={date} onChange={(e) => setDate(e.target.value)} />
        </label>
        <label>
          Status: 
          <input type="text" value={status} onChange={(e) => setStatus(e.target.value)} />
        </label>
        <button type="submit">Save Changes</button>
        <button type="cancel" onClick={closePopup}>Cancel</button>
      </form>
    </div>
  );
};

export default Popup;