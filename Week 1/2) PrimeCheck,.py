## Write a Python function that takes an integer and returns True if it’s a prime number and False otherwise.
from sympy import *
def check(n):
  if isprime(n): return True
  else: return False
a=int(input("Enter first number "))
print(check(a))
