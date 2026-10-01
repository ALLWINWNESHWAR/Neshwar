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