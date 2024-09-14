import { useState } from 'react'
import './App.css'
import NavBar from '../components/NavBar'
import JobList from '../components/JobList'
import jobService from '../services/jobs'

function App() {

  const [jobLists, setJobLists] = useState([])

  return (
    <>
      <NavBar/>
      <JobList/>
    </>
  )
}

export default App
