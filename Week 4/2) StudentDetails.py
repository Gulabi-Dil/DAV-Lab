'''
Question 2:
Create a data frame with details of 10 students and columns as 
Roll Number, Name, Gender, Marks1, Marks2, Marks3. 
a. Create a new column with total marks 
b. Find the lowest marks in Marks1 
c. Find the Highest marks in Marks2 
d. Find the average marks in Marks3 
e. Find student name with highest average 
f. Find how many students failed in Marks2 (<40)
'''
import pandas as pd
details={"Roll Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Yash", "Shah Rukh Khan", "Selmon Bhoi", "Aishwarya Rai", "Katrina Kaif", "Amir Khan", "Chota Bheem", "Bada Bheem", "Jessy", "Dakota"],
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Female"],
    "Marks1": [85, 78, 92, 88, 95, 75, 89, 82, 91, 74],
    "Marks2": [88, 72, 90, 35, 92, 80, 39, 79, 87, 73],
    "Marks3": [91, 79, 88, 84, 90, 78, 86, 80, 93, 72]}
df = pd.DataFrame(details)
df.set_index('Roll Number', inplace=True)
print(df)

df['Total Marks']=df['Marks1']+df['Marks2']+df['Marks3']
print(f"\nAfter adding new column of total marks:\n{df}")

low=df['Marks1'].min()
print(f"\nLowest marks in Marks1: {low}")

high=df['Marks2'].max()
print(f"Highest marks in Marks2: {high}")

avg=df['Marks3'].mean()
print(f"Average marks in Marks3: {avg:.2f}")

df['Average Marks']=df[['Marks1','Marks2','Marks3']].mean(axis=1)
name=df['Average Marks'].idxmax()
highest = df.loc[name, 'Average Marks']
print(f"Student with highest average marks: {df.loc[name, 'Name']} ({highest:.2f} average marks)")

fail2 = len(df[df['Marks2'] < 40])
print(f"Number of students who failed in Marks2: {fail2}")
