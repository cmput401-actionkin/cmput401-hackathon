import React from 'react';
import Job from '../components/Job'
import './JobList.css';

const JobList = () => {

    const jobs = [
        {
            company: 'Company Name 1',
            position: 'Job Position 1',
            resume: 'Resume1.pdf',
            date: '2022-01-01',
            status: 'Applied'
        },
        {
            company: 'Company Name 2',
            position: 'Job Position 2',
            resume: 'Resume2.pdf',
            date: '2022-01-02',
            status: 'Interviewed'
        },
        {
            company: 'Company Name 3',
            position: 'Job Position 3',
            resume: 'Resume3.pdf',
            date: '2022-01-03',
            status: 'Interviewed'
        }
    ];

    const handleJobClick = (job) => {
        // Handle the job click event here...
        console.log(job);
    };

    return (
        <table>
            <thead>
                <tr>
                    <th>Company</th>
                    <th>Position</th>
                    <th>Resume</th>
                    <th>Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {jobs.map((job, index) => (
                    <Job key={index} job={job} onClick={() => handleJobClick(job)} />
                ))}
            </tbody>
        </table>
    )
}

export default JobList