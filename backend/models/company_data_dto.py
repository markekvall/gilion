import pandas as pd
import json
from database.company_data_db_model import CompanyDataDBModel


class CompanyDataDTO:
    def __init__(self, company_name: str = None, daily_data: pd.DataFrame = None, monthly_data: pd.DataFrame = None):
        self.company_name = company_name
        self.daily_data = daily_data
        self.monthly_data = monthly_data

    @classmethod
    def from_db_model(cls, db_model: CompanyDataDBModel):
        daily_data = pd.DataFrame.from_dict(json.loads(db_model.daily_data))
        monthly_data = pd.DataFrame.from_dict(json.loads(db_model.monthly_data))
        return cls(
            company_name=db_model.company_name,
            daily_data=daily_data,
            monthly_data=monthly_data
        )