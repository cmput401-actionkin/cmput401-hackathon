// this script contains all CRUD requests for organization's sake 

// this script is imported to components where the request will be called 


import axios from 'axios'

// e.g. http://localhost:3001/api/jobs 
const baseUrl = 'insert api url here'

const getAll = () => {
    
    // we do a get request using axios asynchronously and it should return a promise (placeholder) until it is fulfilled (i.e. data is received)
    const request = axios.get(baseUrl)

    // once we received the data, we then get the data part of the response and return it (or rather give) to whoever called getAll
    return request.then(response => response.data)
}

const create = (newObject) => {

    // same thing but this time, we give them the newObject that we want to create
    const request = axios.post(baseUrl, newObject)

    // whether the request succeeds/fails, the server will return a http protocol which is in the data for us to return
    return request.then(response => response.data)
}

const update = (id, newObject) => {

    // this time, updating the object requires that we point to the specific id, then we give them the updated version, newObject
    // ${variableName} just a way to access variable values

    const request = axios.update(`${baseUrl}/${id}`, newObject)

    return request.then(response => response.data)
}

export default {
    getAll,
    create,
    update
}