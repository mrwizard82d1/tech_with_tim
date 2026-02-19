import axios from 'axios';

// Create an instance of axios with the base URL of our application
//
// By defining our axios baseURL in a single place, we can use relative
// imports for all components that query our API. Additionally, this
// single definition allows us to change the base URL for **all**
// requests in a single place in the code if necessary.
const api = axios.create({
    baseURL: "http://localhost:8000"
});

// Export the created axios instance
export default api;
