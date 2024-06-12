# 1. assign variable total to store sum
# 2. assign variable count to store number of entries
# 3. request user to enter few numbers and assign them to variable num
# 4. initiate a while loop, check if num is not equal to -1
# 5. update total with inputted number, num
# 6. increment count by one
# 7. continue asking input until user enters -1
# 8. intiate if condition if user enters -1
# 9. calculate average = total/count and store in variable avg
# 10. print total and average using f string and exit while loop, using break


total = 0
count = 0
num = int(input('Enter a few integers and end by typing -1 :'))

while num != -1:
    total += num
    count += 1
    num = int(input('Enter a few integers and end by typing -1 :'))

    if num == -1:
        avg = total/count
        print(f' Total of numbers (excluding -1) entered is {total} and the average is {avg}')
        break