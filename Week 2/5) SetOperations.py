## Write a Python code block to input numbers into two sets. Perform union, intersection, and difference operations on the sets and print the results.
a=input("Enter elements of Set 1: ").split()
a=set(a)
b=input("Enter elements of Set 2: ").split()
b=set(b)
print(f"Union of Set 1 and Set 2 = {a.union(b)}") #Can also use a|b
print(f"Intersection of Set 1 and Set 2 = {a.intersection(b)}") #Can also use a&b
print(f"Difference between Set 1 and Set 2, i.e. Set 1-Set 2 = {a.difference(b)}") #Can also use a-b 
