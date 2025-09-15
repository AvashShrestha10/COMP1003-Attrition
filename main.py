# Avash Shrestha, Student number: 32100429
# Step 1: Load CSV file + Step 2: Data Processing Summaries + Step 3a: Visualization (Pie Chart)

import pandas as pd
import matplotlib.pyplot as plt
# Avash Shrestha, Student number: 32100429
def load_data():
    data = pd.read_csv("nurse_attrition 01 10 2025.csv")
    print("Data loaded successfully! Total records:", len(data))
    return data
# Avash Shrestha, Student number: 32100429
def process_data(data):
    summary = {}
    # Avash Shrestha, Student number: 32100429
    # Total employees
    summary["Total Employees"] = len(data)
    # Avash Shrestha, Student number: 32100429
    # Departments
    summary["Departments"] = list(data["Department"].unique())
    summary["Employees per Department"] = data["Department"].value_counts().to_dict()
    # Avash Shrestha, Student number: 32100429
    # Gender
    summary["Gender Count"] = data["Gender"].value_counts().to_dict()
    # Avash Shrestha, Student number: 32100429
    # Age
    summary["Age"] = {
        "Min": data["Age"].min(),
        "Max": data["Age"].max(),
        "Average": round(data["Age"].mean(), 2)
    }
    # Avash Shrestha, Student number: 32100429
    # Distance from Home
    summary["DistanceFromHome"] = {
        "Min": data["DistanceFromHome"].min(),
        "Max": data["DistanceFromHome"].max(),
        "Average": round(data["DistanceFromHome"].mean(), 2)
    }
    # Avash Shrestha, Student number: 32100429
    # Hourly Rate
    summary["HourlyRate"] = {
        "Min": data["HourlyRate"].min(),
        "Max": data["HourlyRate"].max(),
        "Average": round(data["HourlyRate"].mean(), 2)
    }
    # Avash Shrestha, Student number: 32100429
    # Marital Status %
    summary["MaritalStatus %"] = (
        (data["MaritalStatus"].value_counts(normalize=True) * 100).round(2).to_dict()
    )
    # Avash Shrestha, Student number: 32100429
    # Work Life Balance
    summary["Average WorkLifeBalance"] = round(data["WorkLifeBalance"].mean(), 2)
    # Avash Shrestha, Student number: 32100429
    # Attrition
    summary["Total Attrition"] = data["Attrition"].value_counts().get("Yes", 0)

    return summary

# Avash Shrestha, Student number: 32100429
#  Function for Visualization
def visualize_department_pie(data):
    dept_counts = data["Department"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        dept_counts,
        labels=dept_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Employee Distribution by Department")
    plt.show()

# Avash Shrestha, Student number: 32100429
if __name__ == "__main__":
    df = load_data()
    print(df.head())  # shows first 5 rows

    results = process_data(df)
    for key, value in results.items():
        print(f"{key}: {value}")


    visualize_department_pie(df)
