from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
import pandas as pd

Base = declarative_base()

class CompanyDataDBModel(Base):
    __tablename__ = 'company_data'
    company_name = Column(String, primary_key=True)
    daily_data = Column(JSON)
    monthly_data = Column(JSON)


    @classmethod
    def from_dto(cls, simple_company_data_dto):
        return cls(
            company_name=simple_company_data_dto.company_name,
            daily_data=simple_company_data_dto.daily_data.to_json(),
            monthly_data=simple_company_data_dto.monthly_data.to_json(),
        )