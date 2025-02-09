'''
Question 2: 
For the CEREALS dataset, perform data preprocessing and answer the following questions.
a. Create a table with the 5 number summary of all the numeric attributes.
b. For each of the numeric attributes (proteins upto vitamins) , identify and replace all missing data(indicated with -1) with the arithmetic mean of the attribute.
c. Create a table with the 5 number summary of all the numeric attributes after treating missing values. Do you think the strategy used in dealing with missing values was effective?
d. For each numeric attribute (proteins upto vitamins), identify and replace all noisy data with the median of attribute.
e. Create a table with the 5 number summary of all the numeric attributes after treating noisy values. Do you think the strategy used in dealing with noisy values was effective?
'''
import pandas as pd
import numpy as np

file_path_csv = "/mnt/c/Users/hvpan/Downloads/Cereals1.csv"
df = pd.read_csv(file_path_csv)

numeric_cols = ["protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins"]

# Function to compute the five-number summary
def five_number_summary(df, cols):
    return df[cols].describe(percentiles=[0.25, 0.5, 0.75]).loc[['min', '25%', '50%', '75%', 'max']]

# Compute the initial five-number summary
summary_before = five_number_summary(df, numeric_cols)

# Replace missing values (-1) with the mean of the respective column
for col in numeric_cols:
    mean_value = df[df[col] != -1][col].mean()  # Compute mean excluding -1
    df[col] = df[col].replace(-1, mean_value)

# Compute the five-number summary after handling missing values
summary_after_missing = five_number_summary(df, numeric_cols)

# Function to replace outliers with the median using IQR method
def replace_outliers_with_median(df, cols):
    for col in cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        median_value = df[col].median()

        # Replace outliers with median
        df[col] = df[col].apply(lambda x: median_value if (x < lower_bound or x > upper_bound) else x)

# Replace noisy values with the median
replace_outliers_with_median(df, numeric_cols)

# Compute the five-number summary after handling noisy values
summary_after_noisy = five_number_summary(df, numeric_cols)

# Display the summaries
print("Summary before handling missing values:\n", summary_before)
print("\nSummary after handling missing values:\n", summary_after_missing)
print("\nSummary after handling noisy values:\n", summary_after_noisy)
