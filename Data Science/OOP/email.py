""" 1. create an email simulator using OOP
    2. use python file email.py...task is to build out the class, methods, lists, and functions
    3. declare class Email() with following 
    4. create constructor and pass parameters self and email_address [email address of sender],
    subject_line [subject line] and email_content [contents of email]
    5. add class variable = has_been_read, set it to False
    6. class method to edit email...mark_as_read should change has_been_read to True
    7. add empty variable = inbox of  type list, inbox[]...to store and access email object
    8. add functions: populate_inbox()..creates an email object with the email address,subject line,
    and contents, and stores it in the inbox and populate your inbox with three sample email objects
    9. list_emails()...function loops through the inbox and prints each emails subject_line
    and corresponding number
        Example
        >>0 Welcome to HyperionDev!
        >>1 Great work on the bootcamp!
        >>2 Your excellent marks!
    10.[Optional]-- function extended to read, mark as spam, and delete...using enumerate() function
    11.read_email()...function displays a selected email with email_address, subject_line,
    and email_content and sets its has_been_read instance variable to True
    12.use input from user, read_email(i) prints the email stored at position i
    13.index of 0 will print email with the subject line “Welcome to HyperionDev!”
    14.add logic for menu:
        1. Read an email
        2. View unread emails
        3. Quit application
        
PS. readability of print outputs in mind, communicate with user..make clear email read and executed
example: print(f"\nEmail from {email.email_address} marked as read.\n")
"""

### --- OOP Email Simulator with suggested corrections --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    """Class Email for representing an email"""

    # Declare the class variable, with default value, for emails.
    def __init__ (self,email_address,subject_line,email_content):
        """Constructor method for the class Email"""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Initialise the instance variables for emails.
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        """Method to mark an email as read"""
        self.has_been_read = True

# --- Lists --- #
# Initialised an class variable as empty list to store and access the email objects.
    inbox = []

# --- Functions --- #
# Build out the required functions for your program.

# Function that creates 3 sample emails and adds it to the Inbox list. 
def populate_inbox():
    """function to populate the inbox with emails"""
    emails = [Email('abc1@sweden.com', 'Your excellent marks!', 'Very good progress'),
            Email('def@finland.com', 'Welcome to HyperionDev!', 'Great work on your application'),
            Email('xyz@europe.com', 'Great work on the bootcamp!', 'Well done on your progress')]
    Email.inbox.extend(emails)


# Function that prints the email’s subject_line, along with a corresponding number.
def list_emails():
    """Shows all the email with subject line and respective email number"""
    print('\nYour Inbox:')
    for i, email in enumerate(Email.inbox):
        print(f'{i}. {email.subject_line}')


    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email(index):
    """Displays selected email that is being passed as argument"""
    if 0<= index < len(Email.inbox): # Checks index email number matches to email
        email = Email.inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")

        # Mark the email as read if it hasn't already been read
        if not email.has_been_read:
            email.mark_as_read()
            print(f"\nEmail from {email.email_address} marked as read.\n")

    else:
        print("\nYou have entered an invalid email number.")

def view_unread_emails():
    """Shows all the unread email subject lines with respective numbers"""

    print('\nUnread Emails:')
    for i, email in enumerate(Email.inbox):
        if not email.has_been_read:
            print(f'{i}. {email.subject_line}')

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# --- Main Email Program --- #

# Logic to cover for the various menu operations.
while True:
    user_choice = int(input('''\nWould you like to do:
    1. Read an email
    2. View unread emails
    3. Quit application
    
    Enter your selection: '''))

    # logic to read an email
    if user_choice == 1:
        list_emails()
        index_1 = int(input("Enter number of the email you want to read: "))
        read_email(index_1)

    # logic to view unread emails
    elif user_choice == 2:
        view_unread_emails()

    # logic to quit appplication
    elif user_choice == 3:
        print('Quitting program')
        break

    # exception for any other interger input
    else:
        print("Oops - incorrect input. Please select again")
