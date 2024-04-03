# Gilion App

## Overview

The Gilion app is a full-stack application designed to parse data from two CSV files. The backend is built with FastAPI in Python, utilizing a SQLite database. The frontend is a React TypeScript app styled with MaterialUI.

## Running the Application

To run the application (both frontend and backend), navigate to the root directory (where `docker-compose.yml` is located) and execute the following command:

sudo docker-compose up --build


Ensure you have Docker version 25.0.4 or later installed. This setup has been tested on Ubuntu 22.04 LTS.

Once the application is up and running, access it by navigating to `localhost:3000` in your web browser.

## Backend App

### Description

The backend app parses data from monthly and daily CSV files located in the backend root directory and stores it in the database.

### Endpoints

- **Initial Response**: Retrieve unfiltered daily data from `localhost:8000`. (Note: Only the first 10 objects are sent for demonstration purposes.)
- **Authentication**: All endpoints are protected with authentication. Use username `Alice` and password `My Very Secret Password`.
- **Data Fetching Endpoints**:
  - `localhost:8000/fetch-daily`: Fetch daily data with optional parameters.
  - `localhost:8000/fetch-monthly`: Fetch monthly data with optional parameters.

### Backend Testing

To test the backend directly, use the following URL in your browser:

http://localhost:8000/fetch-daily?start_date=<start_date>&end_date=<end_date>&country_code=<country_code>


Replace `<start_date>`, `<end_date>`, and `<country_code>` with appropriate values.

### Documentation

Explore the Swagger documentation of backend endpoints at [http://localhost:8000/redoc](http://localhost:8000/redoc).

## Frontend App

### Description

The frontend app features a lightmode-darkmode switch for user convenience.

## Thoughts and Observations

- Caching data retrieved from the database were considered. (Saving dataframes from company in memory for other endpoints after first database call.). However i felt it might bring unnecessary complexety to an app of this size. But it is definately a consideration for the future, if we know the user will retrieve many different types of data from different endpoints. Then we can reduce calls to database with that solution.
  
## Future Considerations

- Add rate limiting to endpoints.
- Implement user management and link accessible companies in the database to users.
- Explore orchestration and cloud database solutions.
- Develop line graph functionality for the frontend app.
- Create a POST endpoint to read CSV files and save them to the database.
- Add Update and Delete functionality to the database manager.
