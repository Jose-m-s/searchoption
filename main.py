"""
Search and filter data from the .csv file using Pandas python data analysis library

Usage:
- Ensure that the Pandas library is installed: 'pip install pandas'
- Prepare the .csv file ('Nearabl.Sample.Data_main_us-500.csv') in the same directory as this script.
- Ensure console is in full screen mode to see all of the search fields after search is done.
"""

import pandas as pd

# Load data from the CSV file
df = pd.read_csv('Nearabl.Sample.Data_main_us-500.csv')

# Adds 1 to the default numeric row numbers to align to 500 people
df.index += 1

# Description at the beginning
description = ('\nOptions for the search field (Please print as is): \n'
               'first_name, last_name, company_name,'
               ' address, city, county, state, zip,'
               ' phone1, phone2, email, or web\n')

print(description)

# Validates user's input, ensures correct
valid_search = df.columns.tolist()

while True:

  # Get the search field from the user
  column_to_search = input("Enter the search field: ")

  if column_to_search in valid_search:
    break

  else:
    print(f"Try again. Incorrect search field: '{column_to_search}' \n")

# Get the search term from the user
search_term = input("Enter the search term: ")


# Define a search function
def search_dataframe(search_term, column_name):
  search_result = df[df[column_name].str.contains(search_term, case=False)]
  return search_result


"""
    Search for records in the DataFrame based on a search term and column name.
    
    Parameters:
    - search_term (str): The term to search for.
    - column_name (str): The column to search within.
"""

# Takes inputs and applies them to the search function
result = search_dataframe(search_term, column_to_search)

# Using .value_count() tracks the number of occurrences of the search term
summary = result[column_to_search].value_counts()

# Get the count from summary
search_count = summary.get(search_term, 0)

# Display search results
print("\nSearch Results:\n")

# if statement for no terms related to the search term
if result.empty:
  print(f"No matching record found using the search term: '{search_term}' \n")

# else statement for search terms found in the search field
else:
  print(result, "\n")

  #if there is more than one search term
  if search_count > 1:
    print(
      f"There are {search_count} individuals associated with the search term: '{search_term}'."
    )

  #else if there is only one search term
  elif search_count >= 0:
    print(
      f"There is {search_count} individual associated with the search term: '{search_term}'."
    )
