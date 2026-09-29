'''
6	reshape()
7	flatten(), ravel()
8	Mathematical & statistical functions
9	min(), max(), sum(), mean(), median(), std()
10	Random numbers — random	

'''

# reshape() 
'''
reshape() is one of the most important NumPy functions for Data Science and Machine Learning.
You use it when you want to change the shape/dimensions of an array without changing its data.
'''
#basic 
import numpy as np
sam=np.arange(1,13)

print(sam)
print(sam.shape)        #<-- it has 12 element
