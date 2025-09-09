#author filip kvesic
#date 2 september 2025
#description number 5, is it raining/ windy type thing
raining = input('is it raining: ')
if (raining == 'Yes') or (raining == 'yes') or (raining == 'YES'):
    windy = input('is it windy: ')
    if (windy == 'Yes') or (windy == 'yes') or (windy == 'YES'):
        print('it is too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')
