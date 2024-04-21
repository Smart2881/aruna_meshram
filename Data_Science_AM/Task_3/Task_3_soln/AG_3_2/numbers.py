# 1. request users to input three different numbers
# 2. add all input numbers and print using .format()
# 3. difference of num1 and num2 and print using .format()
# 4. multiply num1, num3 and print using .format()
# 5. add all the numbers then divided by num3 and print

# step 1
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

# step 2
print("Sum of all three numbers : {0}".format(num1 + num2 + num3))

# step 3
print("Difference of number1 and number2 : {0}".format(num1 - num2))

# step 4
print("Multiplcation of number1 and number3 : {0}".format(num1*num3))

# step 5
print("Sum of three and divide by number3 : {0}".format((num1+num2+num3) / num3))