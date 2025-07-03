import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [25, 30, np.nan, 40, 35],
    'Gender': ['F', 'M', 'M', 'M', 'F'],
    'Income': [50000, 60000, 55000, np.nan, 52000],
    'Purchased': ['Yes', 'No', 'Yes', 'No', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# ---- Step 1: Handle Missing Values ----
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Income'].fillna(df['Income'].median(), inplace=True)

# ---- Step 2: Encode Categorical Variables ----
label_enc = LabelEncoder()
df['Gender'] = label_enc.fit_transform(df['Gender'])  # M=1, F=0
df['Purchased'] = df['Purchased'].map({'Yes': 1, 'No': 0})  # binary map

# ---- Step 3: Normalize/Scale Numeric Columns ----
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])

# ---- Step 4: Feature Selection (Drop unnecessary columns) ----
df_final = df.drop(columns=['Name'])

# ---- Final Preprocessed Data ----
print("Preprocessed Data:")
print(df_final)
