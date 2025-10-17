#author filip kvesic
#date 17/10/2025
#description ask user to enter word and modify it
word = input('please enter a word : ')
NewWord = ''
length = len(word)
Variable = ''
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    print(word + 'way')
else:
    for i in range(1,length,1):
        variable = word[i]
        Variable += variable 
        NewWord = Variable+word[0]+'ay'
print(NewWord)
        
    
