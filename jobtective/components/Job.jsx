import React from 'react';
import './Job.css'; // Import the CSS file

const Job = (job) => {
  if (!job) {
    return (
      <tr className="table-row-item">
        <td className="table-cell" colSpan="4">No job data available</td>
      </tr>
    );
  }

  return (
    <tr className="table-row-item">
        <td className="table-cell">{job.companyname || 'N/A'}</td>
        <td className="table-cell">{job.position || 'N/A'}</td>
        <td className="table-cell">{job.resume || 'N/A'}</td>
        <td className="table-cell">{job.date || 'N/A'}</td>
        <td className="table-cell">{job.status || 'N/A'}</td>
    </tr>
  );
};

export default Job;
