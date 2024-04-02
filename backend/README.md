# Gilion app

Frontend and Backend app created to parse data from two csv files.

Backend is a FastAPI python app, using a SQLite database. Frontend is a React Typescript app using MaterialUI theme.

To run application (frontend and backend), navigate to root directory (same as docker-compose.yml) and run "sudo docker-compose up --build".
Im using Docker version 25.0.4 on Ubuntu 22.04 LTS

After app is fully up and running, navigate to localhost:3000.

# Backend app

Data from monthly and daily data gets parsed from csv-files saved in backend root directory and saved in database.
Once app is running, an initial response with unfiltered daily data can be retrieved from localhost:8000. (observe that only the 10 first objects are sent. this is to not slow down the application too much, for demonstration purposes.)

Every endpoint is protected with auth so Alice with her very secret password can access the endpoints. 

monthly and daily data can be fetched from endpoints:
localhost:8000/fetch-daily and /fetch-monthly. These both have parameters: start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None), country_code: Optional[str] = Query(None),

# See swagger documentation of backend endpoints:
http://localhost:8000/redoc


# Frontend app
Make sure to test out the lightmode-darkmode switch. Its sick!


# Thoughts and observations:
- Cashing monthly and daily data retrieved from database was something i considered. However it can lead to unnecessary complexety of the application, if lets say we only would want to use one endpoint in the future.


# Future Considerations:
- Add rate limiting to endpoints
- Add user management and link accessable companies in database to user
- Orchestration and cloud database
- Create line graph for frontend app