'''

Lesson	Topic
1	Series — creation & basics
2	DataFrame — creation & basics
3	Reading CSV files
4	Inspecting data — head(), tail(), info(), describe()
5	Selecting columns
6	Selecting rows — loc[] & iloc[]
7	Filtering data
8	Adding & updating columns
9	Deleting columns/rows
10	Sorting data
11	Missing values — isna(), fillna(), dropna()
12	groupby()
13	Aggregation — sum(), mean(), count(), etc.
14	apply() and custom functions
15	String operations
16	Date & time operations
17	Merge & Join
18	Concatenation
19	Practical Data Analysis
20	🏆 Pandas Mini Project


'''




#Lesson 1: Series
'''
1. what is pandas?
    pandas is a library function used to
        data analysis
        data cleaning
        data manipulation
        working with csv/excel file
        preparing data for machine learning

importing pandas
    import pandas as pd

    
2. What is a Series?
    series is a 1D labeled data structure

3. Creating a Series with Custom Index
    marks = pd.Series(
    [85, 92, 78, 90, 88],
    index=["Arun", "Priya", "Rahul", "Kavi", "Vijay"]
    )
    print(marks)
    
    Arun     85
    Priya    92
    Rahul    78
    Kavi     90
    Vijay    88
'''
import pandas as pd

mark = pd.Series([10,20,30,40,50,60], index=["allwin","balaji","gopal","madhan","sucha","madesh"])
print(mark)
print(mark["allwin"])                       #by key value
print(mark.iloc[0])                         #by position
print(mark + 5)                             #basic calculation
print("sum: ",mark.sum())
print("mean: ",mark.mean())
print("median: ", mark.median())
print("min: ", mark.min())
print("max: ",mark.max())
print("count: ",mark.count())

#q1
