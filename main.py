# Avash Shrestha, Student number: XXXXXXX
# Step 1: Load CSV file

import pandas as pd

def load_data():
    data = pd.read_csv("nurse_attrition 01 10 2025.csv")
    print("Data loaded successfully! Total records:", len(data))
    return data

if __name__ == "__main__":
    df = load_data()
    print(df.head())  # show first 5 rows
