import React, { useState } from 'react';
import Popup from './Popup'; 
import './Job.css';

const Job = ({ job }) => {
  const [currentJob, setCurrentJob] = useState(job);
  const [showPopup, setShowPopup] = useState(false);

  const handleJobUpdate = (updatedJob) => {
    setCurrentJob(updatedJob);
    setShowPopup(false);

    // Placeholder for database update
    console.log('Updating job in database...');
  };

  if (!currentJob) {
    return (
        <tr className="table-row-item">
            <td className="table-cell" colSpan="4">No job data available</td>
        </tr>
    );
  }

  return (
    <>
      <tr className="table-row-item" onClick={() => setShowPopup(true)}>
          <td className="table-cell">{currentJob.company || 'N/A'}</td>
          <td className="table-cell">{currentJob.position || 'N/A'}</td>
          <td className="table-cell">{currentJob.resume || 'N/A'}</td>
          <td className="table-cell">{currentJob.date || 'N/A'}</td>
          <td className="table-cell">{currentJob.status || 'N/A'}</td>
      </tr>
      {showPopup && (
        <>
          <div className="overlay" onClick={() => setShowPopup(false)}></div>
          <Popup job={currentJob} onJobUpdate={handleJobUpdate} closePopup={() => setShowPopup(false)} />
        </>
      )}
    </>
  );
};

export default Job;