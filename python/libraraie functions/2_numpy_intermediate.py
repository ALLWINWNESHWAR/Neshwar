'''
6	reshape()
7	flatten(), ravel()
8	Mathematical & statistical functions
9	min(), max(), sum(), mean(), median(), std()
10	Random numbers — random	

'''
#lesson 6
# reshape() 
'''
reshape() is one of the most important NumPy functions for Data Science and Machine Learning.
You use it when you want to change the shape/dimensions of an array without changing its data.

syntax: array.reshape(rows, columns)
'''
#basic 
import numpy as np
sam=np.arange(1,13)

print("Original:")
print(sam)
print(sam.shape)        #<-- it has 12 element

print("\n2 × 6:")
print(sam.reshape(2, 6))

print("\n3 × 4:")
print(sam.reshape(3, 4))

print("\n4 × 3:")
print(sam.reshape(4, 3))

print("\n6 × 2:")
print(sam.reshape(6, 2))


#1 reshape 
sai=np.arange(1,10)
print("\n3 × 3 Matrix:")
print(sai.reshape(3,3))


#lesson 7
#flatten() and ravel()
'''
These do almost the opposite of reshape().
2D → 1D


flatten()	|   1D array	|   Creates a copy
ravel()	    |   1D array	|   Usually returns a view

'''

arr=np.array([[10,20,30],
            [40,50,60]])

print("original:")
print(arr)

print("\n Flatten:")
print(arr.flatten())

print("\n Ravel: ")
print(arr.ravel())

#Lesson 8 — NumPy Mathematical & Statistical Functions
#sum(), mean(), min(), max(), median(), std()

mark = np.array([70, 85, 90, 65, 95, 80])

print("sum: ", np.sum(mark))
print("Mean: ",np.mean(mark))
print("Min: ",np.min(mark))
print("Max: ",np.max(mark))
print("Median: ",np.median(mark))
print("Standard deviation: ",np.std(mark))

marks=np.array([[80,90,70],
                [60,85,75],
                [90,95,85]])

print("add all:", np.sum(marks))
print("add column vise: ", np.sum(marks, axis=0))
print("add row vise: ", np.sum(marks, axis =1))

