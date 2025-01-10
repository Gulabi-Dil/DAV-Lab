## Write a Python function to add two elements and display the result. The elements can be of type integer, float or string.
def Addition(x,y):
   return x+y

a=input("Enter first element ")
b=input("Enter second element ")
try:
  x=float(a)
  y=float(b)
  sum=Addition(x,y)
  if(str(sum).endswith(".0")): print(int(sum))
  else: print(sum)
except ValueError: print(Addition(a,b))
