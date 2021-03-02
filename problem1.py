#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
P1=(input('Choose a person from the list to replace: ')).strip()
P2=(input('Enter the replacemnt: ')).strip()
dIndex=people.index(P1)
people.remove(P1)
people.insert(dIndex,P2)
print(people)

