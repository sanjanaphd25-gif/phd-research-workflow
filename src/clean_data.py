import pandas as pd
import os

# Define file paths
input_path = os.path.join("data", "sample_data.csv")
output_path = os.path.join("data", "cleaned_data.csv")

def clean_data():
    # Read the CSV file
    df = pd.read_csv(input_path)
    # Detect missing values
    print(df.isnull().sum())

    # Fill missing numeric values with column mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # (Optional) Fill non-numeric missing values with mode
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].mode()[0], inplace=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print(f"\nCleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_data()