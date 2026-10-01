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


#Lesson 9: axis with mean(), min(), and max()
'''
axis=0 → column-wise
axis=1 → row-wise
'''
marks = np.array([
    [80, 90, 70],
    [60, 85, 75],
    [90, 95, 85]
])

#1. Mean with axis
print("mean:", np.mean(marks))
print("mean column-wise:", np.mean(marks, axis=0))
print("mean row-wise:", np.mean(marks, axis=1))
#2. Minimum with axis
print("min:", np.min(marks))
print("min column-wise:", np.min(marks, axis=0))
print("min row-wise:", np.min(marks, axis=1))
#3. Maximum with axis
print("max:", np.max(marks))
print("max column-wise:", np.max(marks, axis=0))
print("max row-wise:", np.max(marks, axis=1))


#Lesson 10: Random Numbers
'''
NumPy provides the np.random module for generating random data.
'''

#1. np.random.randint()
#   syntax : np.random.randint(start, stop)
num = np.random.randint(1, 10)
print(num)

#2. Generate multiple random numbers
#   syntax : np.random.randint(start, stop, size)
num=np.random.randint(1,10,5)
print(num)

#3. Generate a 2D array
num = np.random.randint(1, 100, size=(3, 4))            # <-- 3rows 4 column
print(num)

#4
a=np.random.randint(1,50)
print(a)

#5
b=np.random.randint(1,50,5)
print(b)

#6
c=np.random.randint(1,50, size=(3,3))
print(c)

#6
d=np.random.randint(1,20,5)
print(d)

#np.random.rand()                   <-- it will generate random foloaing numbers between 0 to 1
print(np.random.rand())
print(np.random.rand(5))
print(np.random.rand(3, 4))

#if you want to print more than 1.. then multuply by 10
print(np.random.rand() * 10)

#1. Generate multiple values
print(np.random.rand(5) * 100)

#np.random.uniform()
#1
print(np.random.uniform(10, 50))

#2
print(np.random.rand(5))

#3
print(np.random.rand(2, 4))

#4
print(np.random.uniform(20, 30, 5))


'''
1. Random integer:                              np.random.randint(10, 50)
2. Random decimal:                              np.random.uniform(10, 50)
3. Random decimal between 0 and 1:              np.random.rand()   
'''

'''
randint   → random INTEGER
rand      → random FLOAT 0–1
uniform   → random FLOAT in YOUR range
'''