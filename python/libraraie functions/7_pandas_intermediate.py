"""
1	Series	                                        ✅ Completed
2	DataFrame basics	                            ✅ Completed
3	Reading CSV files	                            ✅ Completed
4	Inspecting data (head, tail, info, describe)	✅ Completed
5	Selecting columns	                            ✅ Completed
6	Selecting rows (loc and iloc)	                ✅ Completed
7	Filtering data	                                ✅ Completed
8	Adding and updating columns	                    ✅ Completed
9	Deleting columns and rows	                    ✅ Completed
10	Sorting data	                                ✅ Completed
11	Missing values	                                ✅ Completed
12	groupby()	                                    ✅ Completed
13	Aggregation functions	                        ✅ Completed
14	apply() and custom functions	                ⏳ Pending
15	String operations	                            ⏳ Pending
16	Date and time operations	                    ⏳ Pending
17	Merging and joining DataFrames	                ⏳ Pending
18	Concatenation	                                ⏳ Pending
19	Practical Data Analysis	                        ⏳ Pending
20	Pandas Mini Project	                            ⏳ Pending

"""

#lesson 10      Sorting Data in Pandas
import pandas as pd

df = pd.read_csv("D:/1 Credo Training/python/csv files/students.csv")

print(df)

#1. Sort by Marks — Ascending Order
print(df.sort_values(by="Marks"))
#2. Sort by Marks — Descending Order
print(df.sort_values(by="Marks", ascending=False))
#3. Sort by Student Name
print(df.sort_values(by="Name"))
#4. Sort by Multiple Columns
print(df.sort_values(by=["Age","Marks"]))
#5. Sort and Update the Original DataFrame
df.sort_values(by="Marks", ascending=False, inplace=True)
print(df)

#Task 1
print("\nTask 1")
df= pd.read_csv("D:/1 Credo Training/python/csv files/students.csv")
print(df.sort_values(by = "Marks"))
print(df.sort_values(by = "Marks", ascending=False))
print(df.sort_values(by="Name"))
print(df.sort_values(by = "Age", ascending=False))
print(df.sort_values(by = ["Age","Marks"], ascending=[True,False]))
print(df.sort_values(by = "City"))
df.sort_values(by = "Marks", ascending=False, inplace=True)
print(df)
print(df.sort_values(by="Marks", ascending=False).head(3))


#Lesson 11 — Handling Missing Values in Pandas
import pandas as pd
import numpy as np

data = {
    "Name": ["Allwin", "Gopi", "Bal", "Sucha", "Mad"],
    "Age": [22, np.nan, 22, np.nan, 24],
    "Marks": [85, 92, np.nan, 90, 88],
    "City": ["Karur", "Chennai", np.nan, "Karur", "Salem"]
}

df = pd.DataFrame(data)

print("\nNull values")
print(df)
print(df.isnull())
a = df.isnull().sum()
print("total number of NULL Value:", a.sum())
print(df[df.isnull().any(axis=1)])
df_cleaned = df.dropna()
print(df_cleaned)
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)


#Lesson 12 — groupby()
print("\nLesson 12 --> Groupby")

import pandas as pd

data = {
    "Name": ["Allwin", "Gopi", "Bal", "Sucha", "Mad", "Ravi"],
    "City": ["Karur", "Chennai", "Erode", "Karur", "Salem", "Chennai"],
    "Marks": [85, 92, 78, 90, 88, 80],
    "Age": [22, 23, 22, 21, 24, 23]
}

df = pd.DataFrame(data)

print(df)

print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Marks"].max())
print(df.groupby("City")["Marks"].agg(["mean", "max", "min", "count"]))                 #<-- agg(["mean","max"])      Aggrefate function

#Task 1
print("\nTask 1 group by")
print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Name"].count())
print(df.groupby("City")["Marks"].max())
print(df.groupby("City")["Marks"].min())
print(df.groupby("City")["Age"].mean())
print(df.groupby("City")["Marks"].agg(["mean","max","min"]))
df1 = df.groupby("City")["Marks"].mean()
print(df1.max())
print(df1.idxmax(), df1.max())                                                      #index max   (idxmax())


#Lesson 13 — Aggregation Functions

#1. Basic aggregation
print(df["Marks"].sum())    # Total marks
print(df["Marks"].mean())   # Average marks
print(df["Marks"].max())    # Highest marks
print(df["Marks"].min())    # Lowest marks
print(df["Marks"].count())  # Number of non-missing marks

#2. Multiple aggregations on one column
print(df["Marks"].agg(["sum", "mean", "max", "min", "count"]))

#3. Aggregation across multiple columns
print(df[["Age", "Marks"]].agg(["mean", "max", "min"]))

#4. Aggregation grouped by city
print(df.groupby("City").agg({"Marks": ["mean", "max"],"Age": ["mean", "min"]}))

#task 1
print("\nTask 1")
print(df["Name"].count())
print("Average Marks:" , df["Marks"].mean())
print("max marks: ", df["Marks"].max() , "\nmin marks: ",df["Marks"].min() )

print(df["Marks"].agg(["sum","mean","max","min","count"]))
print(df[["Age","Marks"]].agg(["mean","max"]))

print(df.groupby("City").agg({"Marks":["mean"],"Age":["mean"]}))

city_avg = df.groupby("City")["Marks"].mean()
print(city_avg.idxmax(), city_avg.max())                                                    # <-- idxmax

