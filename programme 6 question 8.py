#author filip kvesic
#date 6 october 2025
#description guess the number im thinking of and ill tell you how many guess it took
guesses = 1
number = 0
print('guess the number i have in mind ')
while number > 67 or number < 67:
    number = int(input('enter the number: '))
    if number != 67:
        guesses = guesses + 1
        if number < 67:
            print('too low')
        elif number > 67:
            print('too high')
        elif number == 67:
            break
print('well done')
print('it took this many guesses: ', guesses)
