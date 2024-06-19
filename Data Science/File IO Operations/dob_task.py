"""Program to read a txt file (DOB.txt) and
split the names & birthdate and print them in separate sections"""

# used implicit method and open read only DOB.txt file
# use a for loop to split lines in list called content and print first two values for Names
with open('DOB.txt', 'r', encoding="utf-8") as f:
    print('\nNames\n')
    for line in f:
        content = line.split()
        print(f"{content[0]} {content[1]}")


# use same above steps to open file and run a for loop
# split lines in list and print third and fourth value for Birthdate
with open('DOB.txt', 'r', encoding="utf-8") as f:
    print('\nBirthdate\n')
    for dob in f:
        content = dob.split()
        print(f"{content[2]} {content[3]} {content[4]}")
