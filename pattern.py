# 1. request user to input pattern size
# 2. rows asigned as 1 
# 3. columns asigned as size times 2
# 4. initiate a for loop with i range(rows, columns)
# 5. assign variable k = i, add if condition i <= size else cols - i to get number of characters
# 6. initiate a for loop with j range(k)
# 7. print '*' using print() function
# 8. add next line, using empty print()


size = int(input('Enter your pattern size: '))
rows = 1
cols = size * 2


for i in range(rows, cols):
    k = i if i <= size else cols - i
    for j in range(k):
        print('*', end = ' ')
    print()

