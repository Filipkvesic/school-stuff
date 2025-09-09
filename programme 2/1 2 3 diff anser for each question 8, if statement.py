#Author: Filip Kvesic
#Date: 01 September
#Description: 1 2 3 different answer for each
number = input('please enter a number between 1 and 3: ')
number = int(number)
if (number > 3) or (number < 1):
    print('error')
elif (number == 1):
    print('thank you')
elif (number == 2):
    print('well done')
elif (number == 3):
    print('Correct')
