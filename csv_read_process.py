# read a CSV and clean up (potential) issues like 
# blank values, edge whitespaces and quotes, 
# removing leading dollar signs, etc.

import csv

def read_and_process_csv(name_of_file):
    """
    Reads a csv saved in same directory as this python file, 
    replaces any blank values ('') with None, strips edge whitespaces and quotes, 
    and remove leading dollar signs, and 
    returns a list of lists.

    Parameters:
    name_of_file: string of csv file path not including .csv; Windows use double backslash in path.

    Return: a list of lists of strings
    """
    with open(f'{name_of_file}.csv', 'r') as file:
        entries = []
        rows = csv.reader(file)
        for row in rows:
            cleaned_row = [] # after a row is finished and appended to entries, reset to empty list.
            for cell in row:
                # Replace empty strings with None
                if cell == '':
                    cell = None
                else:
                    # strip whitespaces
                    cell_stripped = cell.strip()
                    # To remove all double quotes only from the start and end of a string
                    cell_no_quote = cell_stripped.strip('"')
                    # remove leading dollar sign and convert to float
                    if cell_no_quote.startswith("$"):
                        clean_cell = float(cell_no_quote.lstrip("$"))
                        # TODO: remove commas in Cost number as string.
                    else:
                        clean_cell = cell_no_quote

                cleaned_row.append(clean_cell)

            entries.append(cleaned_row)            

    return entries

file_path = "C:\\Users\\prest\\OneDrive\\Documents\\AIO Python\\personal_projects\\personal_projects\\Expenses Aggregated Copy"
cleaned_entries = read_and_process_csv(file_path)

print(f"first 5 rows of expenses:\n{cleaned_entries[0:6]}")

if __name__ == "__read_and_process_csv__":
    read_and_process_csv("Expenses Aggregated Copy") # TODO: fix this so don't need an argument