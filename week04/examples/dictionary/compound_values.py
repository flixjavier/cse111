#compound values

#**A simple value is a value that doesn’t contain parts, such as an integer. A compound value is a value that has parts, such as a list.

def main():
  # Create a dictionary with student IDs as the keys
  # and student data stored in a list as the values.
  students_dict = {
    # student_ID: [given_name, surname, email_address, credits]
    "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
    "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
    "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
    "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
    "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0]
  }

  #the best way to find an element in a dictionary is usign the following syntax: dictionary_name[id or Key]

  # These are the indexes of the elements in the value lists.
  GIVEN_NAME_INDEX = 0
  SURNAME_INDEX = 1
  EMAIL_INDEX = 2
  CREDITS_INDEX = 3

  total = 0

  # Get a student ID from the user.
  id = input("Enter a student ID: ")

  # Check if the student ID is in the dictionary.
  if id in students_dict:

    # Find the student ID in the dictionary and
    # retrieve the corresponding value, which is a list.
    value = students_dict[id]
    print(value)

    # Retrieve the student's given name (first name) and
    # surname (last name or family name) from the list.
    given_name = value[GIVEN_NAME_INDEX]
    surname = value[SURNAME_INDEX]

    # Print the student's name.
    print(f"{given_name} {surname}")

  else:
    print("No such student")

  #Processing All Items. find the total of credits of all students
  #** processing is different than find an item here we need to use a for loop and dict.items()

  #For each item in the list add the number
  # of credits that the student has earned.
  """ for item in students_dict.items():
    key = item[0]
    value = item [1]
    print(key)
    print(value) """
  for key, value in students_dict.items(): #UNPACKING
    # Retrieve the number of credits from the value list.
    print(key)
    print(value)
    credits = value[CREDITS_INDEX]

    #add the number of cretids to the total
    total += credits

  print(f"Total credits earned by all students: {total}")

  #UNPACKING



# Call main to start this program.
if __name__ == "__main__":
  main()

