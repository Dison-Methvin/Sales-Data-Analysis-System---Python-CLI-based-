class FeatureEngineering:
    @staticmethod
    def add_features(df):
        try:
            # Added new features to the dataframe
            df['Month'] = df['Date'].dt.month
            df['Week'] = df['Date'].dt.isocalendar().week
            df['Profit'] = df['Total'] - df['Tax 5%']
            return df
        except Exception as e:
            print(f"An error occurred during feature engineering: {e}")
            return df
