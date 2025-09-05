#author filip kvesic
#date 5 september 2025
#description number 6, if your 18 you can vote, etc
age = input('what is your age: ')
age = int(age)
if (age >= 18):
    print('you can vote')
elif (age == 17):
    print('you can learn to drive')
elif (age == 16):
    print('you can buy a lottery ticket')
elif (age < 16):
    print('you can go tirck or treating')