# from personal expenses as a CSV, address blank values and analyze expenses.

import csv

def read_csv_addressing_blanks(name_of_file):
    """
    Reads a csv saved in same directory as this python file, 
    replaces any blank values ('') with None, and returns a list of lists.

    Parameters:
    name_of_file: string of csv file name not including .csv

    Return: a list of lists of strings
    """
    with open('data.csv', 'r') as file:
        entries = []
        rows = csv.reader(file)
        for row in rows:
            # Replace empty strings with None or a default value
            cleaned_row = [cell if cell != '' else None for cell in row]
            entries.append(cleaned_row)

    return entries

raw_entries = read_csv_addressing_blanks("Expenses Aggregated Copy")