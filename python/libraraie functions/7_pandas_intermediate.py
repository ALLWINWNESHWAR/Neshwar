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