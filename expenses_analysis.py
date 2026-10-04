# from personal expenses as a CSV, address blank values and analyze expenses.

from csv_read_process import read_and_process_csv
from datetime import datetime as dt
import pandas as pd

file_csv_path = "C:\\Users\\prest\\OneDrive\\Documents\\AIO Python\\personal_projects\\personal_projects\\Expenses Aggregated Copy"
cleaned_entries = read_and_process_csv(file_csv_path)

# print(f"{cleaned_entries[0:6]=}") # first list in list contains headers

# Constants for headers
CATEGORY_INDEX = 0
DATE_INDEX = 1
COST_INDEX = 2
WHAT_INDEX = 3 # 03OCT26 "Name of company or individual; any actual notes"
NOTES_INDEX = 4 # 03OCT26 payment method

# transform data types: index of inner lists, 'heading':type_to_transform_into
# 1, "Date":datetime.date object
    # "full day, full month dd, yyyy" into "%A, %B %d, %Y"
# 2, "Cost":float

date_format = "%A, %B %d, %Y"
try:
    for i in range(1, len(cleaned_entries)): # start from first entry
        # transform each in place in each inner list.
        if cleaned_entries[i][DATE_INDEX] is not None:
            # parse to datetime, then call .date()
            cleaned_entries[i][DATE_INDEX] = dt.strptime(cleaned_entries[i][DATE_INDEX], date_format).date()
        else: continue
        if cleaned_entries[i][COST_INDEX] is not None:
            # Cost to float
            cleaned_entries[i][COST_INDEX] = float(cleaned_entries[i][COST_INDEX])
        else: continue

except ValueError as e:
    print(f"Error at outer list index {i}\n{e}")

# print(f"transformed cleaned_entries[0:6]=\n{cleaned_entries[0:6]}")
# print(f"\ncleaned_entries[199:201]:") 
# for j in range(198, 201):
#     print(f"{cleaned_entries[j]=}")

# Make pandas dataframe (df) from list of lists (from csv reading, cleaning, transformed)
# slice list[1:] for data rows, and table[0] for columns names
df = pd.DataFrame(cleaned_entries[1:], columns=cleaned_entries[0])

# Returns True if 'column_name' has any None/NaN values, otherwise False
has_none_date = df['Date'].isna().any()
has_none_cost = df['Cost'].isna().any()
print(f"{has_none_date=}\n{has_none_cost=}")

#TODO: address groupby dates with None values and sum of Costs
# Can check sums by summing all Costs ignoring any None values

# group by week and sum costs
# freq='W' ends week on Sundays
# without .reset_index(), the dates would be the index. With it, dates are in a standard column, and default integer row index (0,1,2...)
# weekly_cost_df = df.groupby(pd.Grouper(key='Date', freq='W'))['Cost'].sum().reset_index()

# print(f"\n{weekly_cost_df=}")

print("\nGood end!")