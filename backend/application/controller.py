import pandas as pd
from models.simple_company_data_dto import SimpleCompanyDataDTO
from database.database_manager import DatabaseManager


class Controller:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager


    def to_database(self, company_name: str, company_daily: pd.DataFrame, company_monthly: pd.DataFrame):
        
        company_daily_with_c: pd.DataFrame = self._add_value_c(company_daily)
        company_monthly_with_c: pd.DataFrame = self._add_value_c(company_monthly)
        
        company_data_dto: SimpleCompanyDataDTO = SimpleCompanyDataDTO(
            company_name=company_name,
            daily_data=company_daily_with_c,
            monthly_data=company_monthly_with_c,
        )

        self.db_manager.create(company_data_dto)


    def fetch_daily(self, company_name: str, start_date: str = None, end_date: str = None, country_code: str = None) -> pd.DataFrame:

        company_data: SimpleCompanyDataDTO = self.db_manager.read_data_by_company_name(company_name)

        daily_data_df: pd.DataFrame = company_data.daily_data

        filtered_data: pd.DataFrame = self._filter_data(daily_data_df, start_date, end_date, country_code)

        return filtered_data


    def fetch_monthly(self, company_name: str, start_date: str = None, end_date: str = None, country_code: str = None) -> pd.DataFrame:

        company_data: SimpleCompanyDataDTO = self.db_manager.read_data_by_company_name(company_name)

        monthly_data_df: pd.DataFrame = company_data.monthly_data

        filtered_data: pd.DataFrame = self._filter_data(monthly_data_df, start_date, end_date, country_code)
        
        return filtered_data


    def _filter_data(self, df: pd.DataFrame, start_date: str = None, end_date: str = None, country_code: str = None) -> pd.DataFrame:
        if start_date is None and end_date is None and country_code is None:
            return df

        conditions = []
        if start_date is not None:
            conditions.append(df['date'] >= start_date)
        if end_date is not None:
            conditions.append(df['date'] < end_date)
        if country_code is not None:
            conditions.append(df['country_code'] == country_code)

        filtered_df = df
        filtered_df = df
        for condition in conditions:
            filtered_df = filtered_df[condition]

        return filtered_df


    def _add_value_c(self, df: pd.DataFrame) -> pd.DataFrame:
        if 'A' not in df.columns or 'B' not in df.columns:
            raise KeyError("Columns 'A' and 'B' must exist in the DataFrame")

        df = df.copy()
        df['C'] = df['A'] + df['B']
        return df