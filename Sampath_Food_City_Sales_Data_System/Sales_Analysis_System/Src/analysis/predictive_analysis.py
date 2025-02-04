import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd

class PredictiveAnalysis:
    @staticmethod
    def encode_categorical_data(df, categorical_cols):
        try:
            # Encoded categorical data using OneHotEncoder
            encoder = OneHotEncoder(sparse_output=False, drop='first')
            encoded_data = encoder.fit_transform(df[categorical_cols])
            encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))
            return encoded_df
        except Exception as e:
            print(f"An error occurred during categorical data encoding: {e}")
            return pd.DataFrame()

    @staticmethod
    def scale_numerical_data(X):
        try:
            # Scaled numerical data using StandardScaler
            scaler = StandardScaler()
            return scaler.fit_transform(X)
        except Exception as e:
            print(f"An error occurred during numerical data scaling: {e}")
            return np.array([])

    @staticmethod
    def perform_predictive_analysis(df):
        try:
            categorical_cols = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
            encoded_df = PredictiveAnalysis.encode_categorical_data(df, categorical_cols)

            numerical_cols = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'Rating']
            processed_df = pd.concat([df[numerical_cols], encoded_df], axis=1)

            X = processed_df.drop(['Total'], axis=1)
            y = processed_df['Total']

            X_scaled = PredictiveAnalysis.scale_numerical_data(X)

            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            model = Ridge(alpha=1.0)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)

            # Displayed the results of the predictive analysis
            print("\nPredictive Sales Analysis Results:")
            print(f"R² Score: {r2:.4f}")
            print(f"Mean Squared Error: {mse:.4f}")
            print(f"Mean Absolute Error: {mae:.4f}")
        except Exception as e:
            print(f"An error occurred during predictive analysis: {e}")
