#Author: Filip Kvesic
#Date: 01 September
#Description: simple + COMPOUND interest
principle = input('starting money: ')
interest = input('interest: ')
years = input('years: ')
principle = int(principle)
interest = float(interest)
years = int(years)
simple = principle * (1 + (interest * years))
print('simple interest = ',simple)
compound = principle * (1 + interest) ** years
print('compound interest = ',compound)
