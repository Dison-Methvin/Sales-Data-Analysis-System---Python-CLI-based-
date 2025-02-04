import sys
import os

# Added the Src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.data_loader import DataLoader
from analysis.data_cleaning import DataCleaning
from analysis.feature_engineering import FeatureEngineering
from analysis.eda import EDA
from analysis.predictive_analysis import PredictiveAnalysis
from analysis.kpi import KPI
from ui.consoleUI import Helpers
from auth.authentication import Authentication

def display_menu(is_admin):
    # Displayed the main menu options to the user
    menu_options = [
        "1. Load and Clean Data",
        "2. Perform Exploratory Data Analysis (EDA)",
        "3. Perform Predictive Sales Analysis",
        "4. Calculate Key Performance Indicators (KPIs)",
        "5. Monthly Sales Analysis",
        "6. Product Price Analysis",
        "7. Weekly Sales Analysis",
        "8. Product Preference Analysis",
        "9. Distribution of total sales amount of purchases (Sales Distribution Analysis)",
        "10. Branch Specific Analysis",
    ]
    if is_admin:
        menu_options.append("11. Upload New Dataset")
    menu_options.append("0. Logout")
    menu_options.append("99. Exit")
    
    print("\n" + "="*120)
    print("Sampath Food City (PVT) Ltd - Sales Data Analysis Menu".center(120))
    print("="*120)
    for option in menu_options:
        print(option)
    print("="*120)

def handle_choice(choice, df, file_path, is_admin):
    try:
        if choice == '1':
            # Loaded and cleaned the data
            data_loader = DataLoader()
            df = data_loader.load_data(file_path)
            df = DataCleaning.clean_data(df)
            df = FeatureEngineering.add_features(df)
            print("Data loaded and cleaned successfully.")
        elif choice == '2':
            # Performed Exploratory Data Analysis (EDA)
            print("\n" + "="*120)
            print("Exploratory Data Analysis (EDA)".center(120))
            print("="*120)
            EDA.perform_eda(df)
        elif choice == '3':
            # Performed Predictive Sales Analysis
            print("\n" + "="*120)
            print("Predictive Sales Analysis".center(120))
            print("="*120)
            PredictiveAnalysis.perform_predictive_analysis(df)
        elif choice == '4':
            # Calculated Key Performance Indicators (KPIs)
            print("\n" + "="*120)
            print("Key Performance Indicators (KPIs)".center(120))
            print("="*120)
            KPI.calculate_kpis(df)
        elif choice == '5':
            Helpers.monthly_sales_analysis(df)
        elif choice == '6':
            Helpers.product_price_analysis(df)
        elif choice == '7':
            Helpers.weekly_sales_analysis(df)
        elif choice == '8':
            Helpers.product_preference_analysis(df)
        elif choice == '9':
            Helpers.sales_distribution_analysis(df)
        elif choice == '10':
            while True:
                branch = input("\nEnter the branch name for specific analy3sis: ")
                if branch in df['Branch'].unique():
                    Helpers.branch_specific_analysis(df, branch)
                    break
                else:
                    print("Invalid branch. Please try again.")
        elif choice == '11' and is_admin:
            new_file_path = input("Enter the path of the new dataset: ")
            if os.path.exists(new_file_path):
                df = DataLoader.load_data(new_file_path)
                print("New dataset loaded successfully.")
            else:
                print("File not found. Please check the path and try again.")
        elif choice == '0':
            print("Logging out.")
            return False
        elif choice == '99':
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid option. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return True

def main():
    print("="*120)
    print("Sampath Food City (PVT) Ltd - Sales Data Analysis".center(120))
    print("Provided by Data Labs - Leading Software Development Company".center(120))
    print("="*120)
    
    auth_file_path = "C:/Users/dison/OneDrive/Documents/ESOFT - HND  Documents/HND - Applied Programming & Design Principles/Sampath_Food_City_Sales_Data_System/Sales_Analysis_System/Src/auth/users.json"
    
    while True:
        user_type = Authentication.authenticate(auth_file_path)
        if not user_type:
            return
        
        file_path = "C:/Users/dison/OneDrive/Documents/ESOFT - HND  Documents/HND - Applied Programming & Design Principles/Sampath_Food_City_Sales_Data_System/Sales_Analysis_System/Src/data/Sampath_Food_City_Sales_Data.xlsx"
        data_loader = DataLoader()
        df = data_loader.load_data(file_path)
        
        if df is not None:
            # Cleaned and added features to the data
            df = DataCleaning.clean_data(df)
            df = FeatureEngineering.add_features(df)
            
            while True:
                display_menu(user_type == 'admin')
                choice = input("Select an option: ")
                if not handle_choice(choice, df, file_path, user_type == 'admin'):
                    break
    
    print("\n" + "="*120)
    print("End of Analysis".center(120))
    print("="*120)

if __name__ == "__main__":
    main()
