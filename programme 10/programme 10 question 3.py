#author Filip Kvesic
#date 23/10/2025
#description make all of a specific letter $ except the first
string = input('please enter a string: ')
string[0]
new_string = string.replace(string[0], '$')
before_even_newer_string = string[0]
slicing_thing = new_string[1:len(new_string)]
print(slicing_thing)
print(before_even_newer_string+slicing_thing)
