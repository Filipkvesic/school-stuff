#author filip kvesic
#date 6 october 2025
#description keep asking for number until its between 10 and 20
number = 0
while number < 10 or number > 20:
    number = int(input('please enter a number between 10 and 20: '))
    if number > 20:
        print('too big')
    elif number < 10:
        print('too small')
    elif number >= 10 and number <= 20:
        break
print('thank you')
        
