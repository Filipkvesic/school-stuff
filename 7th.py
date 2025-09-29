#Author: Filip Kvesic
#Date: 01 September
#Description: program to request user name as input and return same wit
total_price = input('what is the total price of the bill:  ')
total_price = int(total_price)
number_people = input('how many are dining?:  ')
number_people = int(number_people)
Total = total_price / number_people
print('each person must pay',   Total)