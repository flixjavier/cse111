import csv
STUDENT_DICTIONARY_DATA = "students.csv"
I_NUMBER_INDEX = 0
STUDENT_NAME_INDEX = 1

def main():
  i_number = input('Please enter an I-Number (xxxxxxxxx): ')
  student_dictionary = read_dictionary(STUDENT_DICTIONARY_DATA)

  if i_number in student_dictionary:
    print(student_dictionary[i_number])
  else:
    print("No such student")

def read_dictionary(filename):
  """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
  """
  dictionary = {}

  with open(filename, "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
      if len(line) != 0:
        key = line[I_NUMBER_INDEX]
        value = line[STUDENT_NAME_INDEX]
        dictionary[key] = value  
  # end append file
  return dictionary
  
if __name__ == "__main__":
  main()