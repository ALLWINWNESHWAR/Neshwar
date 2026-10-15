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


    
NOTE:
mean() → Average of all values.
median() → Middle value after sorting.
mode() → Most frequently occurring value.

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
marks = pd.Series([85,92,78,90,88], index=["allwin","gopi","bal","sucha","mad"])
print("sucha marks : ", marks["sucha"])
print("value in pos 1: ", marks.iloc[1])
print("total: ",marks.sum())
print("avg: ", marks.mean())
print("mid: ", marks.median())


#filrering 
print("filtering")
print(marks[marks > 88])
print(marks[marks <=85])
print(marks[marks > 80])
print("between:\n", marks[(marks >=85) & (marks <=92)])

#Lesson 1 — Final Concept: Handling Missing Values
'''
               Function    	          Purpose
            ---------------    ----------------------------
                isna()	        Identifies missing values
                notna()	        Identifies non-missing values
                fillna()	    Fills missing values
                dropna()	    Removes missing values

'''


print("\n")
marks = pd.Series([85, 92, None, 90, 88])
print(marks.isna())                             #if it is NULL return true
print(marks.notna())                            #if it is Not NULL returns true
print(marks.isna().sum())                       #sum no.of null value
print(marks.mean())




#Pandas Lesson 2 — DataFrame
