from tabulate import tabulate

class EDA:
    @staticmethod
    def display_section(title, df):
        # Displayed a section of the EDA results
        print("\n" + "="*120)
        print(title.center(120))
        print("="*120)
        print(tabulate(df, headers='keys', tablefmt='pretty'))

    @staticmethod
    def perform_eda(df):
        try:
            # Performed exploratory data analysis (EDA)
            EDA.display_section("Summary Statistics", df.describe().reset_index())
            EDA.display_section("Checking for Missing Values", df.isnull().sum().reset_index(name='Missing Values'))
            EDA.display_section("Sales by Branch", df.groupby('Branch')['Total'].sum().reset_index())
            EDA.display_section("Profitability by Branch", df.groupby('Branch')['Profit'].sum().reset_index())
            EDA.display_section("Customer Segments (Total Sales by Product Line)", df.groupby(['Customer type', 'Product line'])['Total'].sum().unstack().fillna(0).reset_index())
        except Exception as e:
            print(f"An error occurred during EDA: {e}")
