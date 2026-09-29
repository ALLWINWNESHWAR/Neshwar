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

#First NumPy Practice
import numpy as np

mark=np.array([85,90,76,88,95])

print(mark)
print("dimention:", mark.ndim)
print("shape:", mark.shape)
print("size:", mark.size)
print("data type:", mark.dtype)
print("adding 5 marks:", mark+5)
print("subtraction 5 marks:", mark-5)
print("multiplying 2 marks:", mark*2)
print("dividing 2 marks:", mark/2)

print("\n")
#Lesson 2: NumPy Indexing  (learn how to access individual values.)
print("first mark:",mark[0])
print("last mark:",mark[-1])
#slicing
print(mark[1:3])
print(mark[:3])
print(mark[2:])
print(mark[::2])
print(mark[2::])
print(mark[1:4:2])
print(mark[::-1])

print("\n")
#Lesson 3: 2D NumPy Arrays
    #array[row, column]
std = np.array([
    [85, 90, 76],
    [88, 95, 82],
    [70, 75, 80]
])

print("2d matrix:", std)
print("first row:", std[ 0])
print("first row second element:", std[0,1])

    #2D Indexing
print("Student 2:", std[1])
print("Student 3:", std[2])
print("Student 2, SQL mark:", std[1,1])
print("Student 3, Python mark:", std[2,0])
print("Student 3, ML mark:", std[2,2])


print("\n")
#Lesson 4 — 2D Array Slicing
print("fro 1st row to 2rd and 1st colunm to 3rd column", std[0:2, 0:3])
print("from second row from second colunm:", std[1:3, 1:3])
print("all row first column:",std[:, 0])
print("allrow second column:", std[:, 1])


#Lesson 5 — Creating Special NumPy Arrays
'''
np.zeros()
np.ones()
np.arange()
np.linspace()
'''
print(np.zeros(5))              #create array of containg 5 zeros
print(np.ones(5))               #create array of containing 5 one
print(np.arange(1, 11))         #create array of 1 to 10

print(np.arange(0, 20, 5))
print(np.arange(2, 10, 2))
print(np.arange(10, 0, -2))
print(np.arange(5))