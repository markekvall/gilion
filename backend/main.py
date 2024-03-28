from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException, status, Query, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from application.controller import Controller
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows only requests from react app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()

def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"a"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"a"
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

@app.get("/")
def read_root(credentials: Annotated[HTTPBasicCredentials, Depends(security)],
                start_date: Optional[str] = Query(None),
                end_date: Optional[str] = Query(None),
                country_code: Optional[str] = Query(None)
                ):
    controller = Controller()
    data: pd.DataFrame = controller.fetch_daily(start_date, end_date, country_code).head()
    return data.to_json(orient='records')


#@app.post("/upload")
#async def upload_csv(file: UploadFile = File(...)):
#    if not file.filename.endswith(".csv"):
#        return {"error": "Only CSV files allowed"}
    
    #return df.head().to_dict()

