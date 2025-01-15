import pandas as pd
import os
import matplotlib.pyplot as plt

# Function to load and clean data from an Excel file
def load_and_clean_data(file_path):
    try:
        df = pd.read_excel(file_path, header=3)
        
        # Check if the required columns exist
        required_columns = ['Name of the Instrument', 'ISIN', 'Quantity', 'Market value\n(Rs. in Lakhs)', '% to NAV']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing expected columns in {file_path}: {missing_columns}")
        
        df.dropna(subset=['Name of the Instrument'], how='all', inplace=True)
        df = df[~df['Name of the Instrument'].str.contains('EQUITY|a\\)', na=False)]
        df = df[required_columns]
        df.rename(columns={
            'Market value\n(Rs. in Lakhs)': 'Market Value (Lakhs)',
            '% to NAV': 'Percentage to NAV'
        }, inplace=True)
        return df
    except Exception as e:
        print(f"Error loading and cleaning data from {file_path}: {e}")
        return None

# Function to calculate changes between datasets
def calculate_changes(previous_data, current_data):
    try:
        comparison_df = pd.merge(
            current_data, 
            previous_data, 
            on='Name of the Instrument', 
            suffixes=('_Current', '_Previous')
        )
        
        # Ensure numerical columns are properly converted
        numerical_columns = [
            'Quantity_Current', 'Quantity_Previous', 
            'Market Value (Lakhs)_Current', 'Market Value (Lakhs)_Previous', 
            'Percentage to NAV_Current', 'Percentage to NAV_Previous'
        ]
        for col in numerical_columns:
            comparison_df[col] = pd.to_numeric(comparison_df[col], errors='coerce')
        
        # Compute changes
        comparison_df['Quantity Change'] = comparison_df['Quantity_Current'] - comparison_df['Quantity_Previous']
        comparison_df['Market Value Change (Lakhs)'] = comparison_df['Market Value (Lakhs)_Current'] - comparison_df['Market Value (Lakhs)_Previous']
        comparison_df['Percentage to NAV Change'] = comparison_df['Percentage to NAV_Current'] - comparison_df['Percentage to NAV_Previous']
        
        return comparison_df[['Name of the Instrument', 'ISIN_Current', 'Quantity Change', 'Market Value Change (Lakhs)', 'Percentage to NAV Change']]
    except Exception as e:
        print(f"Error calculating changes: {e}")
        return None

# Function to visualize changes
def visualize_changes(changes_df):
    try:
        changes_df.sort_values(by='Market Value Change (Lakhs)', ascending=False, inplace=True)
        top_n = min(10, len(changes_df))  # Limit the chart to the top 10 changes
        top_changes = changes_df.head(top_n)
        plt.figure(figsize=(12, 8))
        plt.barh(top_changes['Name of the Instrument'], top_changes['Market Value Change (Lakhs)'], color='skyblue')
        plt.xlabel('Market Value Change (Lakhs)')
        plt.ylabel('Instrument')
        plt.title('Top Fund Allocation Changes')
        plt.gca().invert_yaxis()  # Invert y-axis for better readability
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing changes: {e}")

if __name__ == "__main__":
    try:
        # Input from the user
        fund_name = input("Enter fund name (e.g., ZN250): ")
        date_range = input("Enter date range in months (e.g., 5 for last 5 months): ")

        # Collect relevant files based on fund name and date range
        available_files = sorted([f for f in os.listdir() if fund_name in f and f.endswith('.xlsx') and "Fund_Allocation_Changes" not in f])
        if len(available_files) < 2:
            print("Not enough data files for comparison.")
        else:
            all_changes = []
            for i in range(min(len(available_files) - 1, int(date_range))):
                previous_file = available_files[i]
                current_file = available_files[i + 1]

                print(f"Comparing {previous_file} with {current_file}...")
                previous_data = load_and_clean_data(previous_file)
                current_data = load_and_clean_data(current_file)

                if previous_data is not None and current_data is not None:
                    changes_df = calculate_changes(previous_data, current_data)
                    if changes_df is not None:
                        all_changes.append(changes_df)

            combined_changes = pd.concat(all_changes, ignore_index=True)
            output_file = f"Fund_Allocation_Changes_{fund_name}_{date_range}_Months.xlsx"
            combined_changes.to_excel(output_file, index=False)

            print(f"Changes successfully calculated and saved to {output_file}.")
            visualize_changes(combined_changes)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

