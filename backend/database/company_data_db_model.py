from sqlalchemy import Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CompanyDataDBModel(Base):
    __tablename__ = 'company_data'
    company_name = Column(String, primary_key=True)
    daily_data = Column(JSON)
    monthly_data = Column(JSON)


    @classmethod
    def from_dto(cls, company_data_dto):
        daily_data_json = company_data_dto.daily_data.to_json() if company_data_dto.daily_data is not None else None
        monthly_data_json = company_data_dto.monthly_data.to_json() if company_data_dto.monthly_data is not None else None
        return cls(
            company_name=company_data_dto.company_name,
            daily_data=daily_data_json,
            monthly_data=monthly_data_json,
        )