#Author Filip Kvesic
#date 4 september 2025
#description 2 numbers compare
print('please enter two numbers that arent equal')
first = input('first number: ')
second = input('second number: ')
first = int(first)
second = int(second)
if (first==second):
    print('your not supposed to have two equal numbers ):')
elif (first>second):
    print(second,first)
elif (first<second):
    print(first,second)