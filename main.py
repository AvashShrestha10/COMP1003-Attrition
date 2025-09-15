# Avash Shrestha, Student number: 32100429
# Step 1: Load CSV file + Step 2: Data Processing Summaries

import pandas as pd

def load_data():
    data = pd.read_csv("nurse_attrition 01 10 2025.csv")
    print("Data loaded successfully! Total records:", len(data))
    return data

def process_data(data):
    summary = {}

    # Total employees
    summary["Total Employees"] = len(data)

    # Departments
    summary["Departments"] = list(data["Department"].unique())
    summary["Employees per Department"] = data["Department"].value_counts().to_dict()

    # Gender
    summary["Gender Count"] = data["Gender"].value_counts().to_dict()

    # Age
    summary["Age"] = {
        "Min": data["Age"].min(),
        "Max": data["Age"].max(),
        "Average": round(data["Age"].mean(), 2)
    }

    # Distance from Home
    summary["DistanceFromHome"] = {
        "Min": data["DistanceFromHome"].min(),
        "Max": data["DistanceFromHome"].max(),
        "Average": round(data["DistanceFromHome"].mean(), 2)
    }

    # Hourly Rate
    summary["HourlyRate"] = {
        "Min": data["HourlyRate"].min(),
        "Max": data["HourlyRate"].max(),
        "Average": round(data["HourlyRate"].mean(), 2)
    }

    # Marital Status %
    summary["MaritalStatus %"] = (
        (data["MaritalStatus"].value_counts(normalize=True) * 100).round(2).to_dict()
    )

    # Work Life Balance
    summary["Average WorkLifeBalance"] = round(data["WorkLifeBalance"].mean(), 2)

    # Attrition
    summary["Total Attrition"] = data["Attrition"].value_counts().get("Yes", 0)

    return summary

if __name__ == "__main__":
    df = load_data()
    print(df.head())  # show first 5 rows

    results = process_data(df)
    for key, value in results.items():
        print(f"{key}: {value}")
