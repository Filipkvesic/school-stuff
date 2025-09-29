#Author: Filip Kvesic
#Date: 01 September
#Description: program to request user name as input and return same with a greeting
number = input('enter a number: ')
number = int(number)
if (number <= 20) and (number >= 10):
    print('thank you')
elif (number < 10):
    print('incorrect value entered')
elif (number > 20):
    print('incorrect value entered')
