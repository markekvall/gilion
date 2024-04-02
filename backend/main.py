from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from application.controller import Controller
from database.database_manager import DatabaseManager
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"Alice"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"My Very Secret Password"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.on_event("startup")
async def startup_event():

    db_manager = DatabaseManager(create_engine('sqlite:///company_data.db'))
    app.controller = Controller(db_manager)

    daily_data_df: pd.DataFrame = pd.read_csv("daily.csv")
    monthly_data_df: pd.DataFrame = pd.read_csv("monthly.csv")

    app.controller.to_database(company_name="AI Quantum Innovations co.", company_daily=daily_data_df, company_monthly=monthly_data_df)


#@app.post(/instert-csv)


@app.get("/", summary="Fetch daily data for company data available for user on start-up")
def read_root(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                controller: Controller = Depends(lambda: app.controller)
                ):
    """
    Retrieve all daily data available for user on app startup.

    ### Returns:
    - **company_data**: JSON representation of the retrieved daily data.
    **Note:** Only the first 10 company data objects are sent through this api, to make it more speedy for demonstration purposes. 
    """
    data: pd.DataFrame = controller.fetch_daily(company_name="AI Quantum Innovations co.").head(10)
    return {"company_data": data.to_json(orient='records')}


@app.get("/fetch-daily", summary="Fetch daily data with filters")
def read_daily(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                start_date: Optional[str] = Query(None),
                end_date: Optional[str] = Query(None),
                country_code: Optional[str] = Query(None),
                controller: Controller = Depends(lambda: app.controller)
                ):
    """
    Retrieve daily data with optional filters for the company available for user.

    This endpoint retrieves daily data for the company available for user with optional filters.

    ### Query Parameters:
    - **start_date** (optional): Start date for filtering the data (format: "YYYY-MM-DD").
    - **end_date** (optional): End date for filtering the data (format: "YYYY-MM-DD").
    - **country_code** (optional): Country code for filtering the data.

    ### Returns:
    - **company_data**: JSON representation of the retrieved daily data.
    """
    data: pd.DataFrame = controller.fetch_daily(company_name="AI Quantum Innovations co.", start_date=start_date, end_date=end_date, country_code=country_code)
    return {"company_data": data.to_json(orient='records')}


@app.get("/fetch-monthly", summary="Fetch montly data with filters")
def read_monthly(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                start_date: Optional[str] = Query(None),
                end_date: Optional[str] = Query(None),
                country_code: Optional[str] = Query(None),
                controller: Controller = Depends(lambda: app.controller)
                ):
    """
    Retrieve monthly data with optional filters for the company available for user.

    This endpoint retrieves monthly data for the company available for user with optional filters.

    ### Query Parameters:
    - **start_date** (optional): Start date for filtering the data (format: "YYYY-MM-DD").
    - **end_date** (optional): End date for filtering the data (format: "YYYY-MM-DD").
    - **country_code** (optional): Country code for filtering the data.

    ### Returns:
    - **company_data**: JSON representation of the retrieved monthly data.
    """
    data: pd.DataFrame = controller.fetch_monthly(company_name="AI Quantum Innovations co.", start_date=start_date, end_date=end_date, country_code=country_code)
    return {"company_data": data.to_json(orient='records')}

