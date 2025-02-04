import pandas as pd

class DataCleaning:
    @staticmethod
    def clean_data(df):
        try:
            df.dropna(inplace=True)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.drop(['Invoice ID'], axis=1)
            return df
        except Exception as e:
            print(f"An error occurred during data cleaning: {e}")
            return df
