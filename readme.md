**Mutual Fund Allocation Change Tracker**

**Project Overview**

This project is a Python framework to analyze changes in mutual fund allocations over time. It provides insights into changes in fund holdings for specific mutual funds, allowing users to track allocation trends across different months.

**Key Features**

Tracks mutual fund allocation changes based on uploaded monthly portfolio files.

Allows users to specify a fund name and a date range (in months).

Outputs insights into changes in fund holdings, including:

- Percentage changes in allocation.
- Quantity and market value changes.
- Detailed breakdown by month.
- Supports customizable visualizations using Matplotlib.

**Requirements**

Before running this project, ensure you have the following installed:

- Python 3.7 or later
- Libraries:
  - pandas
  - matplotlib
  - openpyxl (for reading .lsx files)

**Setup**

1\.Clone this repository:

Copy code

- git clone https://github.com/your\_username/mutual-fund-tracker.git
- cd mutual-fund-tracker

2\.Install required libraries:

- pip install -r requirements.txt

3\.Place your monthly portfolio files in the project directory. Example:

- ZN250 - Monthly Portfolio September 2024.xlsx
- ZN250 - Monthly Portfolio November 2024.xlsx

**Run the script:**

python excel.py
