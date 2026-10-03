# from personal expenses as a CSV, address blank values and analyze expenses.

from csv_read_process import read_and_process_csv
from datetime import datetime as dt

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
        # parse to datetime, then call .date()
        cleaned_entries[i][DATE_INDEX] = dt.strptime(cleaned_entries[i][DATE_INDEX], date_format).date()
        # Cost to float
        cleaned_entries[i][COST_INDEX] = float(cleaned_entries[i][COST_INDEX])

except ValueError as e:
    print(f"Error at outer list index {i}\n{e}")

# print(f"transformed cleaned_entries[0:6]=\n{cleaned_entries[0:6]}")
print(f"\ncleaned_entries[199:201]") 
#TODO: need fix indecies 0,1. transformed cleaned_entries[199] = ['credit card', 'credit card', '12.00', 'Venmo', 'debit Silvia']
for j in range(198, 201):
    print(f"{cleaned_entries[j]=}")

print(f"{cleaned_entries[192]=}")

print("\nGood end!")