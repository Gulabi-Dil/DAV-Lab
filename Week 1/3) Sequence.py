## Create a Python function that creates a sequence between 1 and 100 and prints all the odd numbers. Compute and display the sum of all the even numbers.
from sympy import *
def Seq():
  return [x for x in range(1,101) if x%2==1]
for n in Seq(): print(n, end=" ")
s=sum([x for x in range(1,101) if x%2==0])
print("\nSum of all even numbers in range = ",s)
