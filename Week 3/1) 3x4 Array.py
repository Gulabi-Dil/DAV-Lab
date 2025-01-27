'''
Generate a 3x4 NumPy array with random integers between 1 and 50.   
a. Calculate and print the Mean, Median, and Standard Deviation of the array 
b. Print the Sum of all elements and the sum of each row. 
c. Reshape the 3x4 array into a 2x6 array and print it. 
'''
import numpy as np
import random
arr=np.random.randint(1,51,size=(3,4))
print(f"Original array is:\n{arr}")
mn=np.mean(arr)
md=np.median(arr)
dev=np.std(arr)
print(f"a.\nMean = {mn}\nMedian = {md}\nStandard Deviation = {dev}\n")
s=np.sum(arr)
s1=np.sum(arr,axis=1)
print(f"b.\nSum of all elements = {s}\nSum of each row:\n{s1}\n")
newarr=arr.reshape(2,6)
print(f"c. After reshaping into a 2x6 array:\n{newarr}")
