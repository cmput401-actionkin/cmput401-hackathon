import { useState, useEffect } from 'react'
import './App.css'
import NavBar from '../components/NavBar'
import JobList from '../components/JobList'
import jobService from '../services/jobs'

function App() {

  const [jobs, setJobs] = useState([])

  // used for handling asynchronous activity; were calling the GET request in the script 
  useEffect(() => {
    jobService
      .getAll()
      .then(initialJobs => {
        setJobs(initialJobs)
      })

  // empty array indicates that this useeffect is only run once after initial render; if no empty array, run every render
  }, [])

  return (
    <>
      <NavBar/>
      <JobList/>
    </>
  )
}

export default App
