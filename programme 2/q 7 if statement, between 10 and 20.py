#author filip kvesic
#date 5 september 2025
#description number 7, number between 10 and 20, too low too high
number = input('enter a number: ')
number = int(number)
if (number <= 20) and (number >= 10):
    print('correct')
elif (number < 10):
    print('too low')
elif (number > 20):
    print('too high')
