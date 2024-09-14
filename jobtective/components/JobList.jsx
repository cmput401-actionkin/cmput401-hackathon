import Job from '../components/Job'

const JobList = (jobs) => {
    
    console.log(jobs)
    
    return (
        <>
            {
                jobs && jobs.length > 0 ?
                    jobs.map( job => {
                        <Job job = {job} />
                    })
                : <p> No Jobs Available</p>
            }
        </>
    )
}

export default JobList