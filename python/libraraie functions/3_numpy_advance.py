#Lesson 13 — NumPy Sorting & Searching

"""
np.sort()                       Returns a sorted copy. It doesn't change the original array.
np.argsort()                    
np.argmax()                     Returns the index of the largest value.
np.argmin()                     Returns the index of the smallest value.     
np.where()

"""

import numpy as np

num=np.array([85, 60, 95, 72, 88])

#1 ascending order
print(np.sort(num))
#2 decending oreder
print(np.sort(num)[::-1])
#3 maximum value's index
print(np.argmax(num))
#4 minimum value's index
print(np.argmin(num))
#5actual highest mark using argmax()
print(np.max(num))                      #normal method
print(num[np.argmax(num)])              #using argmax()




#Lesson 14 — np.where()

marks=np.array([85,60,95,72,88])

#find which marks are greater than 80
print(np.where(marks>80))                       #returns index value when the condition is True
print(marks[marks > 80])                        #returns the value greater than 80

print(np.where(marks < 70))
print(marks[marks < 70])

#another use in where
#syntax:    np.where(condition, value_if_true, value_if_false)
result = np.where(marks < 70, "Fail", "Pass")
print(result)

#1print if pass else fail
marks = np.array([45, 78, 92, 55, 88, 63])
re=np.where(marks >=60, "pass", "Fail")
print(re)



#Lesson 15 — Joining NumPy Arrays
'''
np.concatenate()                                    It joins the two arrays together.
np.vstack()                                         vstack means vertical stacking.
np.hstack()                                         hstack means horizontal stacking.

'''

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#1 join two array
re= np.concatenate((a,b))
print(re)

#2 horizantal stacking
re=np.hstack((a,b))
print(re)

#3 vertical stacking
re=np.vstack((a,b))
print(re)


#Lesson 16 — Joining 2D Arrays with axis

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.concatenate((a,b), axis = 0))              # add row
print(np.concatenate((a,b), axis = 1))              # add column
print(np.vstack((a, b)))                            # same as axis = 0



#Lesson 17 — Splitting Arrays
#split()
arr = np.array([10,20,30,40,50,60,70,80])

re = np.split(arr,4)
print(re)

#There are 5 elements, but 5 cannot be divided equally into 2 parts. so we go to        
#array_split()

arr = np.array([10,20,30,40,50])

result = np.array_split(arr, 2)
print(result)


#2D spliting
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

result = np.split(arr, 2)
print(result)

#by axis spliting
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(np.split(arr,2,axis=0))
print(np.split(arr,2,axis=1))





#Lesson 18 — Practical NumPy Data Science Exercises.
#Exercise 1 — Student Marks Analysis

marks = np.array([78, 92, 65, 88, 55, 95, 72, 81, 60, 90])

#Q1. Find the average mark.
print("average mark: ", np.mean(marks))
#Q2. Find the highest mark.
print("higest mark: ", np.max(marks))
#Q3. Find the lowest mark.
print("Lowest mark:", np.min(marks))
#Q4. Find how many students scored 80 or above.
print("std above 80:", marks[(np.where(marks >=80))])
print("std above 80:", len(marks[(np.where(marks >=80))]))
#Q5. Create a result array where:
    #60 or above → "Pass"
    #Below 60 → "Fail"
print("result array:", np.where(marks>=60, "Pass", "Fail"))


#Exercise 2 — Employee Salary Analysis
salary = np.array([
    25000, 32000, 45000, 28000, 52000,
    38000, 60000, 41000, 30000, 55000
])

#Q1. Average salary
print("average salary: ",np.mean(salary))
#Q2. Highest salary
print("high salary: ", np.max(salary))
#Q3. Lowest salary
print("low salary: ", np.min(salary))
#Q4. How many employees earn more than 40,000?
print("employees earn more than 40,000: ", len(salary[salary>40000]))
#Q5. Extract all salaries between 30,000 and 50,000.
print("slary between 30k to 50k:", salary[(salary > 30000) & (salary < 50000)])             #array[(condition1) & (condition2)]



#Exercise 3 — Sales Data Analysis
sales = np.array([
    12000, 18000, 15000, 22000, 30000,
    17000, 25000, 28000, 14000, 20000
])

#Q1. Find the total sales.
print("total sale:", np.sum(sales))
#Q2. Find the average sales.
print("average salae:", np.mean(sales))
#Q3. Find the highest sales.
print("high sale:", np.max(sales))
#Q4. Find the lowest sales.
print("low sale:", np.min(sales))
#Q5. How many sales transactions are above ₹20,000?
print("above 20k:", len(sales[sales>20000]))
#Q6. Extract all sales between ₹15,000 and ₹25,000,
print("between 15k to 25k:", sales[(sales > 15000) & (sales < 25000)])
#Q7. Create a category array:
    #Sales >= 20,000 → "High"
    #Sales < 20,000 → "Low"
print("array: ", np.where(sales >= 20000, "High", "Low"))












"""

Introduction, arrays & properties	                    ✅ Completed
2	Indexing & 1D slicing	                            ✅ Completed
3	2D arrays & indexing	                            ✅ Completed
4	2D slicing	                                        ✅ Completed
5	zeros(), ones(), arange()	                        ✅ Completed
6	reshape()	                                        ✅ Completed
7	flatten(), ravel()	                                ✅ Completed
8	Mathematical & statistical functions	            ✅ Completed
9	min(), max(), sum(), mean(), median(), std()	    ✅ Completed
10	Random numbers — random	                            ✅ Completed
11	Sorting & searching	                                ✅ Completed
12	Conditional selection / Boolean indexing	        ✅ Completed
13	Array joining & splitting	                        ✅ Completed
14	Broadcasting	                                    🔄 
15	Copy vs View	                                    ⏳
16	Practical Data Science exercises	                ⏳
17	NumPy mini project	                                ⏳

"""