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
print(mark.iloc[1])                         #by position
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
print("\nfiltering")
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


print("\nhandling null value")
marks = pd.Series([85, 92, None, 90, 88])
print(marks.isna())                             #if it is NULL return true
print(marks.notna())                            #if it is Not NULL returns true
print(marks.isna().sum())                       #sum no.of null value
print(marks.mean())



print("\nLesson 2 DataFrame")
#Pandas Lesson 2 — DataFrame
#  A data frame is a 2D, tabulated data structure constists of rows and column
# creating data frame]

data = {"name" : ["alwin","gopi","bal","sucha","mad"],
        "age" : [23,22,21,22,23],
        "marks" : [99,90,95,97,98]}

print("dictionary format: ",data)

df = pd.DataFrame(data)

print(df)

# creating dataframe using list

data2 = [["allwin", 22, 99],
         ["balaji", 21, 98],
         ["gopal",  23, 90]]

print(data2)

df = pd.DataFrame(data2, index=["std1","std2","std3"], columns=["name","age","marks"])

print(df)


print("\n")
#4. Accessing DataFrame Columns

data = {"name": ["allwin", "balahi","madhan","gopal","sucha"],
        "age" : [22,23,12,25,22],
        "marks" : [99,90,98,97,96]}

print(pd.DataFrame(data))
print(pd.DataFrame(data["name"]))
print("\n")
df = pd.DataFrame(data)
print(df)
print(df["name"])
print("marks\n",df["marks"])
#mean
print("mean mark: ", df["marks"].mean())
#shape
print("shape : ", df.shape)                                     #shape = 5 x 3
#print no.of rows 
print("Rows: ", df.shape[0])
#print no.of column 
print("column: ", df.shape[1])

#6. Understanding columns, index, and dtypes
#A. Column names
print(df.columns)
print(df.columns.tolist())

#B. Row indexes
print(df.index)

#C. Data types
print("\nData types")
print(df.dtypes)

