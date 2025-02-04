from tabulate import tabulate
import pandas as pd

class Helpers:
    @staticmethod
    def display_analysis(title, analysis_df):
        # Displayed the analysis results in a formatted table
        print("\n" + "="*120)
        print(title.center(120))
        print("="*120)
        print(tabulate(analysis_df, headers='keys', tablefmt='pretty'))

    @staticmethod
    def monthly_sales_analysis(df):
        try:
            # Performed monthly sales analysis
            monthly_sales = df.groupby(['Branch', 'Month'])['Total'].sum().reset_index()
            Helpers.display_analysis("Monthly Sales Analysis of Each Branch", monthly_sales)
        except Exception as e:
            print(f"An error occurred during monthly sales analysis: {e}")

    @staticmethod
    def product_price_analysis(df):
        try:
            # Performed product price analysis
            product_price_analysis = df.groupby('Product line').agg(
                Total_Sales=('Total', 'sum'),
                Average_Unit_Price=('Unit price', 'mean'),
                Quantity_Sold=('Quantity', 'sum')
            ).reset_index()
            Helpers.display_analysis("Price Analysis of Each Product", product_price_analysis)
        except Exception as e:
            print(f"An error occurred during product price analysis: {e}")

    @staticmethod
    def weekly_sales_analysis(df):
        try:
            # Performed weekly sales analysis
            weekly_sales = df.groupby('Week')['Total'].sum().reset_index()
            Helpers.display_analysis("Weekly Sales Analysis of the Supermarket Network", weekly_sales)
        except Exception as e:
            print(f"An error occurred during weekly sales analysis: {e}")

    @staticmethod
    def product_preference_analysis(df):
        try:
            # Performed product preference analysis
            product_preference = df.groupby('Product line')['Total'].sum().reset_index().sort_values(by='Total', ascending=False)
            Helpers.display_analysis("Product Preference Analysis (Sales by Product Line)", product_preference)
        except Exception as e:
            print(f"An error occurred during product preference analysis: {e}")

    @staticmethod
    def sales_distribution_analysis(df):
        try:
            # Performed sales distribution analysis
            bins = [0, 500, 1000, 1500, 2000, 2500, 3000, df['Total'].max()]
            labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000+']
            df['Sales_Range'] = pd.cut(df['Total'], bins=bins, labels=labels)
            sales_distribution = df['Sales_Range'].value_counts().reset_index()
            sales_distribution.columns = ['Sales Range', 'Number of Transactions']
            Helpers.display_analysis("Analysis of the Distribution of Total Sales Amount of Purchases", sales_distribution)
        except Exception as e:
            print(f"An error occurred during sales distribution analysis: {e}")

    @staticmethod
    def branch_specific_analysis(df, branch):
        try:
            if branch not in df['Branch'].unique():
                print(f"Branch '{branch}' does not exist in the dataset.")
                return

            branch_df = df[df['Branch'] == branch].copy()
            # Performed branch-specific analysis
            Helpers.monthly_sales_analysis(branch_df)
            Helpers.product_price_analysis(branch_df)
            Helpers.weekly_sales_analysis(branch_df)
            Helpers.product_preference_analysis(branch_df)
            
            max_total = branch_df['Total'].max()
            bins = [0, 500, 1000, 1500, 2000, 2500, 3000, max_total]
            labels = ['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500', '2500-3000', '3000+']
            branch_df['Sales_Range'] = pd.cut(branch_df['Total'], bins=bins, labels=labels)
            sales_distribution = branch_df['Sales_Range'].value_counts().reset_index()
            sales_distribution.columns = ['Sales Range', 'Number of Transactions']
            Helpers.display_analysis("Branch Specific Analysis for " + branch, sales_distribution)
        except Exception as e:
            print(f"An error occurred during branch specific analysis: {e}")
