import pandas as pd


class Controller:

    def fetch_daily(self, start_date: str, end_date:str, country_code:str) -> pd.DataFrame:
        df = pd.read_csv("daily.csv") #read from database in the future
        filtered_data: pd.DataFrame = self._filter_data(df, start_date, end_date, country_code)

        return filtered_data


    def fetch_monthly(self, start_date: str, end_date:str, country_code:str):
        df = pd.read_csv("monthly.csv") #read from database in the future
        filtered_data: pd.DataFrame = self._filter_data(df, start_date, end_date, country_code)
        
        return filtered_data


    def _filter_data(self, df: pd.DataFrame, start_date: str, end_date:str, country_code:str) -> pd.DataFrame:
        filtered_df = df[(df['date'] >= start_date) & (df['date'] < end_date) & (df['country_code'] == country_code)]
        
        return filtered_df




controller = Controller()

start_date = '2015-01-01'
end_date = '2016-01-01'
country_code = 'AU'

data: pd.DataFrame = controller.fetch_daily(start_date, end_date, country_code)

#filtered_df['C'] = filtered_df['A'] + filtered_df['B']

print(data.head())