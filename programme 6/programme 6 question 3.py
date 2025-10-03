#author filip kvesic
#date 3rd of october
#description take integer number and output all even numbers starting with 0 to the number
number = int(input('please enter a number: '))
even_number = 0
Even_number = 0
while even_number < number:
    if even_number + 1 == number:
        break
    even_number = even_number + 2
    print(even_number)
