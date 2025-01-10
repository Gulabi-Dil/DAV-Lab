## Write a Python code block that inputs a sentence from the user. Count the frequency of each word in the sentence and store the result in a dictionary. Prints the dictionary with words as keys and their frequencies as values. 
from collections import Counter
s=input("Enter a sentence: ").split()
print("Frequencies of words in the sentence:\n",dict(Counter(s)))
