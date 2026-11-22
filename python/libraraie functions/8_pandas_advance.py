import pandas as pd


#Lesson 16 — Date and Time Operations in Pandas


data = {
    "Name": ["Allwin", "Gopi", "Bal", "Sucha", "Mad"],
    "Joining_Date": [
        "2026-01-15",
        "2025-12-20",
        "2026-03-10",
        "2025-11-05",
        "2026-02-25"
    ]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())

print()

print(df.dtypes)

#Convert strings into datetime
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
print(df.dtypes)

#Extract year, month and day
df["Year"] = df["Joining_Date"].dt.year
df["Month"] = df["Joining_Date"].dt.month
df["Day"] = df["Joining_Date"].dt.day
print(df)

#Extract day name
print("\nExtract day name")

df["Day_Name"] = df["Joining_Date"].dt.day_name()
print(df)

#Extract month name
print("\nExtract month name")

df["Month_Name"] = df["Joining_Date"].dt.month_name()
print(df)

print()
data = {"a": 10, "b": 20, "c": 30}

for key in data:
    if data[key] > 15:
        data[key] += 5

print(data)
def update_list(items):
    items.append(100)
    items = [200, 300]

numbers = [10, 20, 30]

update_list(numbers)

print(numbers)