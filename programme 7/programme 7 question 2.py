#author filip kvesic 
# date 8/10 2025
# count how many positive and negative numbers
number = 0
negative = 0
positive = 0

while True:
    number = int(input('please enter some numbers: '))
    if number == 0:
        break
    if number < 1:
        negative = negative + 1
    elif number > -1:
        positive = positive + 1
print('there is', positive, ' positive numbers and', negative, ' negative numbers')
        