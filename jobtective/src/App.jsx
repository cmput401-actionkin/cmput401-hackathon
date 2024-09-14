import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Job from '../components/Job'
import NavBar from '../components/NavBar'

function App() {

  const [jobLists, setJobLists] = useState([])

  return (
    <>
      <NavBar/>
      <Job/>
    </>
  )
}

export default App
