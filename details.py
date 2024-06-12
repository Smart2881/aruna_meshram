# kept all code clean as possible using PEP 8 style guide 😊
# request user to input name
# request user to input age
# request user to input house number
# request user to input street name
# print welcome statement with name, age, house number and street name
# using str.format() method to add variables all in a single sentence


name = input("What is your name : ")

age = int(input("What is your age : "))

house_number = int(input("What is your house number : "))

street_name = input("What is your street name : ")


print("Hello {0}! Welcome! You are {1} years old and live at {2} {3}.".format(
    name, age, house_number, street_name))