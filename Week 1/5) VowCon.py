## Write a Python function that takes a string input from the user and counts the number of vowels and consonants in the string.
def count(s):
 c=0
 v=0
 for i in s:
  if i in "aeiouAEIOU": c+=1
  else: v+=1
 return c,v
a=input("Enter a string: ")
print("number of consonants and vowels respectively: ", count(a))
