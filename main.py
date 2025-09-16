# Avash Shrestha, Student number: 32100429
# Step 1: Load CSV file + Step 2: Data Processing Summaries + Step 3: Visualizations + Step 4: Export Results

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# ------------------ Load Data ------------------
def load_data():
    data = pd.read_csv("nurse_attrition 01 10 2025.csv")
    print("Data loaded successfully! Total records:", len(data))
    return data

# ------------------ Process Data ------------------
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

# ------------------ Visualizations ------------------
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

def visualize_marital_status_bar(data):
    marital_counts = data["MaritalStatus"].value_counts()

    plt.figure(figsize=(6, 4))
    plt.bar(marital_counts.index, marital_counts.values, color=["skyblue", "lightgreen", "salmon"])
    plt.xlabel("Marital Status")
    plt.ylabel("Number of Employees")
    plt.title("Employees by Marital Status")
    plt.show()

# ------------------ Export Summary ------------------
def export_summary(summary, filename="summary_results.txt"):
    with open(filename, "w") as f:
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")
    print(f"Summary exported successfully to {filename}")

# ------------------ Dashboard ------------------
def show_dashboard(data, summary):
    # Create Tkinter window
    root = tk.Tk()
    root.title("Avash Shrestha - Student ID: 32100429 - Dashboard")
    root.geometry("500x400")

    # Title
    title_label = tk.Label(root, text="Employee Engagement Dashboard", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Show key metrics
    metrics_frame = ttk.Frame(root)
    metrics_frame.pack(pady=10)

    metrics = [
        f"Total Employees: {summary['Total Employees']}",
        f"Departments: {', '.join(summary['Departments'])}",
        f"Attrition (Total): {summary['Total Attrition']}",
        f"Average Age: {summary['Age']['Average']}",
        f"Average Hourly Rate: {summary['HourlyRate']['Average']}",
        f"Average Work-Life Balance: {summary['Average WorkLifeBalance']}"
    ]

    for m in metrics:
        lbl = tk.Label(metrics_frame, text=m, font=("Arial", 11))
        lbl.pack(anchor="w")

    # Buttons for charts + export
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=20)

    btn_pie = ttk.Button(btn_frame, text="Show Department Pie Chart", command=lambda: visualize_department_pie(data))
    btn_pie.grid(row=0, column=0, padx=10)

    btn_bar = ttk.Button(btn_frame, text="Show Marital Status Bar Chart", command=lambda: visualize_marital_status_bar(data))
    btn_bar.grid(row=0, column=1, padx=10)

    btn_export = ttk.Button(btn_frame, text="Export Summary", command=lambda: export_summary(summary))
    btn_export.grid(row=1, column=0, columnspan=2, pady=10)

    # Run the Tkinter loop
    root.mainloop()

# ------------------ Main ------------------
if __name__ == "__main__":
    df = load_data()
    print(df.head())  # shows first 5 rows

    results = process_data(df)
    for key, value in results.items():
        print(f"{key}: {value}")

    # Launch dashboard
    show_dashboard(df, results)
