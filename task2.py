#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
myList=[]
Word1=(input('enter a word ')).strip()
Word2=(input('enter a word ')).strip()
Word3=(input('enter a word ')).strip()
Word4=(input('enter a word ')).strip()
Word5=(input('enter a word ')).strip()
myList.append(Word1)
myList.append(Word2)
myList.append(Word3)
myList.append(Word4)
myList.append(Word5)
print(myList)



