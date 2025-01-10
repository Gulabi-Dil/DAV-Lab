## Write a Python code block to create a tuple with five elements. Try to change one of the elements and handle the error that occurs. Print a message that explains why the error occurred.
print("Enter 5 numbers to store in tuple: ")
l=[]
for _ in range(5):
  l.append(int(input()))
b=tuple(l)
print("Trying to change ",l[2]," to \"hello\" in the tuple...")
try:
  b[2]="hello"
except TypeError:
  print("Error occured. Tuple is immutable hence cannot be modified.")
