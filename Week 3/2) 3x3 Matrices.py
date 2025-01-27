'''
Create two (3 * 3) matrices using NumPy and print it. 
Perform and print the results of the following linear algebra operations
a. Matrix addition 
b. Matrix subtraction 
c. Matrix multiplication (element-wise and dot product) 
d. Transpose of a matrix 
e. Determinant and inverse (if applicable)
'''
import numpy as np
a=input("Enter integer numbers for 3x3 matrix A: ").split()
b=input("Enter integer numbers for 3x3 matrix B: ").split()
arr1=np.array(a,dtype=int).reshape(3,3)
arr2=np.array(b,dtype=int).reshape(3,3)
print(f"Matrix A:\n{arr1}\nMatrix B:\n{arr2}\n")
s=np.add(arr1,arr2)
d=np.subtract(arr1,arr2)
p=np.multiply(arr1,arr2)
do=np.dot(arr1,arr2)
tr1=np.transpose(arr1)
tr2=np.transpose(arr2)
d1=np.linalg.det(arr1)
d2=np.linalg.det(arr2)
c1,c2=True,True

print(f"a.\nMatrix A + Matrix B=\n{s}\nb.\nMatrix A - Matrix B =\n{d}\nc.\nMatrix multiplication (element-wise) =\n{p}")
print(f"Matrix multiplication(dot product) =\n{do}")
print(f"d.\nTranspose of Matrix A =\n{tr1}\nTranspose of Matrix B =\n{tr2}\ne.\nDeterminant of Matrix A=\n{d1}\nDeterminant of Matrix B=\n{d2}")
try: 
    i1=np.linalg.inv(arr1)
except np.linalg.LinAlgError:
    print("Matrix A is not invertible.")
    c1=False
try: 
    i2=np.linalg.inv(arr2)
except np.linalg.LinAlgError:
    print("Matrix B is not invertible.")
    c2=False
if(c1): print(f"Inverse of Matrix A=\n{i1}")
if(c2): print(f"Inverse of Matrix B=\n{i2}")
