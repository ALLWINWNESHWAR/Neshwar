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