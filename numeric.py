import pandas as pd

# Sample DataFrame with categorical features
data = {
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'City': ['New York', 'Paris', 'London', 'Paris'],
    'Purchased': ['Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# --- Label Encoding (for binary columns like Gender, Purchased) ---
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Purchased'] = df['Purchased'].map({'Yes': 1, 'No': 0})

# --- One-Hot Encoding (for non-binary categorical like City) ---
df = pd.get_dummies(df, columns=['City'], prefix='City')

print("\nNumeric Data:")
print(df)
