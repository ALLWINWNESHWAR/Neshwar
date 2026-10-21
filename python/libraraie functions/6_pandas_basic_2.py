"""
1	Series	                                        ✅ Completed
2	DataFrame basics	                            ✅ Completed
3	Reading CSV files	                            ✅ Completed
4	Inspecting data (head, tail, info, describe)	✅ Completed
5	Selecting columns	                            ⏳ Pending
6	Selecting rows (loc and iloc)	                ⏳ Pending
7	Filtering data	                                ⏳ Pending
8	Adding and updating columns	                    ⏳ Pending
9	Deleting columns and rows	                    ⏳ Pending
10	Sorting data	                                ⏳ Pending
11	Missing values	                                ⏳ Pending
12	groupby()	                                    ⏳ Pending
13	Aggregation functions	                        ⏳ Pending
14	apply() and custom functions	                ⏳ Pending
15	String operations	                            ⏳ Pending
16	Date and time operations	                    ⏳ Pending
17	Merging and joining DataFrames	                ⏳ Pending
18	Concatenation	                                ⏳ Pending
19	Practical Data Analysis	                        ⏳ Pending
20	Pandas Mini Project	                            ⏳ Pending

"""

import pandas as pd

import os

print(os.getcwd())

#usinf r string (r) --> (backward slash)
df = pd.read_csv(
    r"D:\1 Credo Training\python\csv files\students.csv"
)
print(df)

#normal method (forward slash / )
df = pd.read_csv(
    "D:/1 Credo Training/python/csv files/students.csv"
)
print(df)

#print only specific columns
df = pd.read_csv("D:/1 Credo Training/python/csv files/students.csv",
                 usecols = ["Name", "Marks"] )

print(df)

'''
#reading without header
df = pd.read_csv("D:/1 Credo Training/python/csv files/students.csv", header = None)
print(df)

#providing own column name
df = pd.read_csv("D:/1 Credo Training/python/csv files/students.csv", header=None, names= ["name", "age", "marks", "city"])
print(df)
'''



# Task 1
print(df["Marks"].mean())

df = pd.read_csv("D:/1 Credo Training/python/csv files/students.csv")
print(df.shape)

#Q3 — Find Unique Cities
print(df["City"].unique())

#Q4 — Select Specific Columns
print(df[["Name","Age"]])

#Q5 — Display the First Three Rows
print(df.head(3))

#Display the total number of students.
print("Total stds = ", df["Name"].count())
#Calculate the highest mark.
print("max marks = ", df["Marks"].max())
#Calculate the average mark.
print("avg marks = ", df["Marks"].mean())
#Display students whose marks are greater than 85.
print("marks > 85 : \n", df[df["Marks"] > 85 ])
#Display only the Name and Marks columns for those students.
print(df[df["Marks"] > 85][["Name","Marks"]])


#Lesson 4 — Inspecting Data
print("\nLesson 4 — Inspecting Data")
print("\nfirst 2 rows")
print(df.head(2))

print("\nlast 3 rows")
print(df.tail(3))

print("\ninfo")
df.info()                                   # <-- dont need to use print keyword

print("\ndescribe")
print(df.describe())
print(df["Age"].describe())
#include text columns
print(df.describe(include="all"))

print("\nshape")
print(df.shape)
print("rows", df.shape[0])
print("columns", df.shape[1])

print("\ncolumn name")
print(df.columns)                           # <-- normal method
print(df.columns.tolist())                  # <-- as list format 

print("\ncheck data types")
print(df.dtypes)

#Task 1
print("satistical summary of marks=\n" , df["Marks"].describe())
print(df.dtypes)
print(df.columns.tolist())

#Task 2
print(df.head(3))
print(df.tail(2))
print("rows:", df.shape[0])
print("columns:", df.shape[1])
print(df.describe())
print(df.columns.tolist())
print(df.dtypes)


#Lesson 5 — Selecting Columns in Pandas
print("\nsingle column --> series")
print(df["Age"])
print(df["City"])

print("\nmultiple columns --> dataframe")
print(df[["Name", "Marks"]])
print(df[["Name", "Age", "City"]])

#Tak 1
print(df["Marks"])
print(df[["Name", "City"]])
print(df[["Age", "Marks", "City"]])
print(df[["Name"]])