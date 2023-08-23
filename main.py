import pandas as pd
# from IPython.display import display, HTML

# Load data from a CSV file
df = pd.read_csv('Nearabl.Sample.Data_main_us-500.csv')

# Adds 1 to the default numeric row numbers
df.index = df.index + 1

print("\nOptions for search field include:")
print(
  "first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, or web \n"
)

#Asks which of the search fields to look at
column_to_search = input("Enter the search field: ")

#Asks what search term to look out for
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

result = search_dataframe(search_term, column_to_search)

# Display search results
print("\nSearch Results:\n")
print(result)
