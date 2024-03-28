from sqlalchemy import JSON, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4

Base = declarative_base()

class DatabaseModel(Base):
    __tablename__ = 'company_data'

    id = Column(String, primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, default=datetime.now())
    user_id = Column(String)
    total_amount = Column(String)
    date_of_purchase = Column(String)