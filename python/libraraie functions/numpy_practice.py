'''
arr.ndim        ndim  → How many dimensions?
arr.shape       shape → How is it structured?
arr.size        size  → How many elements?
arr.dtype       dtype → What type of data?
'''

'''
1. what is numpy 
        numpy = numerical python
        it is python library function used to
            numerical function
            matrix function
            mathematical operaation
            working with arrays
            data science
            machine learning
        eg: number[10,20,30,40] this is list
        import numpy as np
        num=np.array([10,20,30,40,50])

2. installing numpy
        In colap numpy is already installed
        In VS code editor --> pip install numpy

3. imporing NumPy
        import numpy as np
            numpy  --> library name
            np     --> alias
4. Creating a NumPy Array           
        1D array
            import numpy as np
            arr-np.array([10,20,30,400,50])
5. 2D array
            import numpy as np
            arr = np.array([[10,20,30],
                            [40,50,60]])

6. 3D array
            import numpy as np
            ar=np.array([
                        [
                            [10,20],
                            [30,40],    ],
                        [   [50,60],
                            [70,80]
                                    ]
                                        ])    

7. importing array properties
    arr=np.array([[10,20,30],[40,50,60]])
    print(arr.ndim)                                 <-- it returns no.of dimentions o/p : 2D
    print(arr.shape)                                <-- Returns the number of rows and columns. o/p: (2 rows, 3 column)
    print(arr.size)                                 <-- Returns the total number of elements. o/p: 6
    print(arr.dype)                                 <-- returns data type.  o/p: int64

8. NumPy Array vs Python List
    a=[10,20,30,40]
    print(a*2)                              <--o/p: [10,20,30,40,10,20,30,40]  

    a=np.array([10,20,30,40])
    print(a*2)                              <--o/p: [20,40,60,80]


       
'''

import numpy as np
num=np.array([10,20,30,40,50])
print(num)
print(type(num))