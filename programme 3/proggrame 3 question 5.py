#Author: Filip Kvesic
#Date: 29 September
#Description: Set a variable called total to 0. Ask the user to enter five numbers. After each input ask if they wish to add that number to the total. If they do, add the number else do not add the number. When they have entered five numbers, display the total.

total = 0

for Q1 in range(5):
    number = int(input('enter a number: '))
    Q = input('do you want to add that number: ')
    if (Q == 'yes') or (Q == 'Yes') or (Q == 'YES'):
        total = total + number
    else:
        pass
print(total)
