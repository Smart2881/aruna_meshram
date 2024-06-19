""" Program allows user to register students for an exam venue
Step 1. Asks the user how many students are registering
Step 2. Create a for loop that runs for that number of students
Step 3. Each time the loop runs the program asks the user to enter the next student ID number. 
Step 4. Write each of the ID numbers to a text file called reg_form.txt
Step 5. Added a dotted line after each student ID in the attendance register, for them to sign
"""

# used implicit method to write in file
# asked user to input number of students, added a venue name and page title, using f string
with open ("reg_form.txt", "w", encoding="utf-8") as file:
    venue = input("Enter exam venue name: ")
    file.write(f"Exam Venue:- {venue}\n\n")
    user = int(input("How many students are registering : "))
    file.write(f"Attendance Register:- {user} Students\n\n")

# used for loop to input student id for the required number of students
# written all the information into a reg_form.txt file, with a dotted new line for signature
    for i in range(user):
        student_id = input("Enter a student id number: ")
        file.write(f"{i+1}) Student id number: {student_id}\n\n\n")
        file.write("................................................\n\n")
