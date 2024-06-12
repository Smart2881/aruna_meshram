# 1. request user input, save string in variable str_manip
# 2. calculate and print string length using len() function
# 3. find last character and replace with '@' character
# 4. print last three letters in reverese order
# 5. sliced first three and last two letters
# 6.concatenate them and print

# steps 1, 2
str_manip =input("Please enter a sentence: ")
length = len(str_manip)
print("Lenght of your sentence is {0} characters".format(length))

# step 3
last_char = (str_manip [-1])
manip_line = str_manip.replace (last_char, "@")
print("Maniplutated output1: {0}".format(manip_line))

# step 4
print("Maniplutated output2: {}".format(str_manip[-1:-4:-1]))

# steps 5, 6
print("Maniplutated output3: {}".format(str_manip[0:3] + str_manip[-2:]))