class KPI:
    @staticmethod
    def calculate_kpis(df):
        try:
            # Calculated key performance indicators (KPIs)
            avg_transaction_value = df['Total'].mean()
            total_revenue = df['Total'].sum()
            gross_margin = df['Profit'].sum() / total_revenue * 100

            print("\nKey Performance Indicators (KPIs):")
            print(f"Average Transaction Value: {avg_transaction_value:.2f}")
            print(f"Total Revenue: {total_revenue:.2f}")
            print(f"Gross Margin: {gross_margin:.2f}%")
        except Exception as e:
            print(f"An error occurred during KPI calculation: {e}")
