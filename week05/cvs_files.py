import csv

# Indexes of some of the columns
# in the dentists.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 3
NUM_PATIENTS_INDEX = 4

# Index of the phone number column
# in the dentists.csv file.
PHONE_INDEX = 2

def main():
  """ # Open the CSV file for reading and store a reference
  # to the opened file in a variable named csv_file.
  with open("hymns.csv", "rt") as csv_file:

    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)

    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row_list in reader:
      print(row_list)

#Processing Each Row in a CSV File
#*skips the first row: next()

# Open a file named dentists.csv and store a reference
  # to the opened file in a variable named dentists_file.
  with open("dentists.csv", "rt") as dentists_file:

    # Use the csv module to create a reader
    # object that will read from the opened file.
    reader = csv.reader(dentists_file)

    # The first row of the CSV file contains column
    # headings and not data about a dental office,
    # so this statement skips the first row of the
    # CSV file.
    next(reader)

    running_max = 0
    most_office = None

    # Read each row in the CSV file one at a time.
    # The reader object returns each row as a list.
    for row_list in reader:

      # For the current row, retrieve the
      # values in columns 0, 3, and 4.
      company = row_list[COMPANY_NAME_INDEX]
      num_employees = int(row_list[NUM_EMPS_INDEX])
      num_patients = int(row_list[NUM_PATIENTS_INDEX])

      # Compute the number of patients per
      # employee for the current dental office.
      patients_per_emp = num_patients / num_employees

      # If the current dental office has more
      # patients per employee than the running
      # maximum, assign running_max and most_office
      # to be the current dental office.
      if patients_per_emp > running_max:
        running_max = patients_per_emp
        most_office = company

  # Print the results for the user to see.
  print(f"{most_office} has {running_max:.1f}"
          " patients per employee") """
  
  #*Reading a CSV File into a Compound List
  # Read the contents of the dentists.csv file
  # into a compound list.
  dentists_list = read_compound_list("dentists.csv")

  # Print the entire list.
  print(dentists_list)

  #*Reading a CSV File into a Compound Dictionary

  # Read the contents of the dentists.csv into a
  # compound dictionary named dentists_dict. Use
  # the phone numbers as the keys in the dictionary.
  dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

  # Print the dentists compound dictionary.
  print(dentists_dict)


#Reading a CSV File into a Compound List
def read_compound_list(filename):
  """Read the contents of a CSV file into a compound
  list and return the list. Each element in the
  compound list will be a small list that contains
  the values from one row of the CSV file.

  Parameter filename: the name of the CSV file to read
  Return: a list of lists that contain strings
  """
  # Create an empty list that will
  # store the data from the CSV file.
  compound_list = []

  # Open the CSV file for reading and store a reference
  # to the opened file in a variable named csv_file.
  with open(filename, "rt") as csv_file:

    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)

    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row_list in reader:

      # If the current row is not blank,
      # append it to the compound_list.
      if len(row_list) != 0:

        # Append one row from the CSV
        # file to the compound list.
        compound_list.append(row_list)

  # Return the compound list.
  return compound_list

#*Reading a CSV File into a Compound Dictionary
def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.

  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  # Create an empty dictionary that will
  # store the data from the CSV file.
  dictionary = {}

  # Open the CSV file for reading and store a reference
  # to the opened file in a variable named csv_file.
  with open(filename, "rt") as csv_file:

    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)

    # The first row of the CSV file contains column
    # headings and not data, so this statement skips
    # the first row of the CSV file.
    next(reader)

    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row_list in reader:

      # If the current row is not blank, add the
      # data from the current to the dictionary.
      if len(row_list) != 0:

        # From the current row, retrieve the data
        # from the column that contains the key.
        key = row_list[key_column_index]

        # Store the data from the current
        # row into the dictionary.
        dictionary[key] = row_list
        
  # Return the dictionary.
  return dictionary




# Call main to start this program.
if __name__ == "__main__":
  main()