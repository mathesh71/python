import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age': [25, 30, 200, np.nan, 35, 25],   # 200 is an outlier
    'Income': [50000, 60000, 55000, 52000, np.nan, 50000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# --- Step 1: Handle Nulls ---
# Option 1: Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Income'].fillna(df['Income'].mean(), inplace=True)

# --- Step 2: Remove Outliers (IQR method) ---
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df = remove_outliers(df, 'Age')
df = remove_outliers(df, 'Income')

# --- Step 3: Remove Duplicates ---
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)
