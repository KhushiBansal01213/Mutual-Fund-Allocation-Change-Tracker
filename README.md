# Mutual-Fund-Allocation-Change-Tracker
Project Overview
This project is a Python framework to analyze changes in mutual fund allocations over time. It provides insights into changes in fund holdings for specific mutual funds, allowing users to track allocation trends across different months.

Key Features
Tracks mutual fund allocation changes based on uploaded monthly portfolio files.
Allows users to specify a fund name and a date range (in months).
Outputs insights into changes in fund holdings, including:
Percentage changes in allocation.
Quantity and market value changes.
Detailed breakdown by month.
Supports customizable visualizations using Matplotlib.
Requirements
Before running this project, ensure you have the following installed:

Python 3.7 or later
Libraries:
pandas
matplotlib
openpyxl (for reading .xlsx files)
Setup
Clone this repository:

bash
Copy code
git clone https://github.com/your_username/mutual-fund-tracker.git
cd mutual-fund-tracker
Install required libraries:

bash
Copy code
pip install -r requirements.txt
Place your monthly portfolio files in the project directory. Example:

ZN250 - Monthly Portfolio September 2024.xlsx
ZN250 - Monthly Portfolio November 2024.xlsx
Usage
Run the script:

bash
Copy code
python excel.py
Follow the prompts:

Enter the date range (in months, e.g., 5 for last 5 months).
Provide file paths for the monthly portfolio data.
Example Output:

A report showing allocation changes:
Increases or decreases in holdings.
Percentage of NAV changes.
Month-by-month breakdown.
Visualization of allocation trends.
File Structure
bash
Copy code
mutual-fund-tracker/
│
├── excel.py                  # Main Python script
├── requirements.txt          # Required Python libraries
├── README.md                 # Project documentation
└── data/                     # Folder for input .xlsx files (optional)
Key Functions
load_and_clean(filepath): Loads and preprocesses mutual fund portfolio data.
compare_allocations(df1, df2, date1, date2): Compares allocation changes between two datasets.
generate_insights(df, fund_name)

