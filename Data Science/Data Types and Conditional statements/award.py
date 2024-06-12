# 1. request user input for Triathlon timings
# 2. for swimming, cycling and running in minutes
# 3. add all the numbers and print total
# 4. added conditions for qualifying time 

# steps 1, 2
swimming = int(input('Enter swim time in minutes: '))
cycling = int(input('Enter cycling time in minutes: '))
running = int(input('Enter running time in minutes: '))

# step 3
triathlon = (swimming + cycling + running)
print(f'Total triathlon time in minutes: {triathlon}')

# step 4
qualifying_time = triathlon
if 0 <= qualifying_time <= 100:
    print('Qualifying Award for participant is Provincial colours')
     
elif 101 <= qualifying_time <= 105:
    print ('Qualifying Award for participant is Provincial half colours')

elif 106 <= qualifying_time <= 111:
    print('Qualifying Award for participant is Provincial scroll')

else:
    print('No award')