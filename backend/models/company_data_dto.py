from pydantic import BaseModel, Field, Field
from datetime import datetime
from typing import Optional
from uuid import uuid4
import pandas as pd


class CompanyDataDTO(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), description="Receipt id")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(), description="datetime of digital receipt creation")
    company_name: Optional[str] = Field(description="Name of company which data is extracted from", default=None)
    daily_data: Optional[pd.DataFrame] = Field(description="Data diplaying values A, B and C in daily form", default=None)
    monthly_data: Optional[pd.DataFrame] = Field(description="Data diplaying values A, B and C in monthly form", default=None)
