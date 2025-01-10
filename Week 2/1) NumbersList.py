## Write a Python code block that inputs numbers into a list. Print the largest, smallest, the sum, and the average of the numbers. Count occurrences of a specific number in the list.
n=int(input("Enter number of numbers: "))
l=[]
for _ in range(n):
  l.append(int(input()))
print("Largest: ",max(l))
print("Smallest: ",min(l))
sum=0
for i in l: sum+=i
print("Sum: ",sum)
print("Average: ",(sum/n))
k=int(input("Enter a number to search in list: "))
print("Number of occurences in list: ",l.count(k))
