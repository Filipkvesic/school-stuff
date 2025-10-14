#author filip kvesic
#date 14/10/2025
#description get number, find digits, maske digits to create a new number
first_number = input('please enter the first number:  ')
first_number_numerical = int(first_number)
digits = len(first_number)
thingy = (10) ** (digits - 1)
total = first_number_numerical // thingy
print(digits,total)
    
    
    