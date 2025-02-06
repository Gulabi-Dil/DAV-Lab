'''
Question 1:
Create a Series from a list of integers representing daily temperatures (in Celsius) over a week. 
Assign index labels as day of the week. 
a. Find and print the average (mean) temperature for the week. 
b. Identify and print the maximum and minimum temperatures and their respective days. 
c. Display the temperatures greater than a specific value. 
d. Convert all temperatures to Fahrenheit. 
e. Print the days had temperatures above the average. 
'''
import pandas as pd
temp = [12, 16, 20, 15, 21, 17, 19]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ts = pd.Series(temp, index=days, name="Temperature (°C)")
print(ts)

avg = ts.mean()
print(f"\nAverage temperature = {avg:.2f} °C\n")

minimum = ts.min()
maximum = ts.max()
daymin = ts.idxmin()
daymax = ts.idxmax()
print(f"Minimum temperature: {minimum} °C on {daymin}")
print(f"Maximum temperature: {maximum} °C on {daymax}\n")

print(f"Temperatures greater than 15 °C:\n{ts[ts > 15]}\n")

tf = ts * (9/5.0) + 32
print(f"Temperatures in Fahrenheit:\n{tf.to_string()}")
abavg = ts[ts > avg]
print(f"\nDays with temperatures above the average:\n{abavg.index.to_list()}")
