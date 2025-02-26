# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Derek Klock,2/25/2025,Completed Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Error: File must exist prior to running script.  Check the folder location \
and the spelling of the file name.")
    print("-- Technical Error Message --")
    print(e.__doc__, type(e), sep='\n')
    print("")

except Exception as e:
    print("Error: There was a non-specific error.")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
    print("")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("Error: Student name should only contain letters.")

            except ValueError as e:
                print(e)
                print("-- Technical Error Message --")
                print(e.__doc__, type(e), sep="\n")
                print("")

            except Exception as e:
                print("Error: There was a non-specfic error.")
                print(e.__doc__, type(e), sep="\n")
                print("")

            else:
                break

        while True:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("Error: Student name should only contain letters.")

            except ValueError as e:
                print(e)
                print("-- Technical Error Message --")
                print(e.__doc__, type(e), sep="\n")
                print("")

            except Exception as e:
                print("Error: There was a non-specfic error.")
                print("-- Technical Error Message --")
                print(e, e.__doc__, type(e), sep="\n")
                print("")

            else:
                break

        course_name = input("Please enter the name of the course: ")

        student_data = {"FirstName": student_first_name, "LastName": student_last_name,\
                        "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name}\
 for {course_name}.")
        for row in students:
            print(row)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        for row in students:
            print(f"Student {row["FirstName"]} {row["LastName"]} is enrolled\
 in {row["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
            print("The following data was saved to file!")
            for row in students:
                print(f"Student {row["FirstName"]} {row["LastName"]} is enrolled\
 in {row["CourseName"]}")
            continue

        except PermissionError as e:
            print("Error: Could not write to file.  File not saved")
            print("-- Technical Error Message --")
            print(e.__doc__, type(e), sep="\n")
            print("")

        except Exception as e:
            print("Error: There was a non-specfic error.  File not saved")
            print("-- Technical Error Message --")
            print(e.__doc__, type(e), sep="\n")
            print("")

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
