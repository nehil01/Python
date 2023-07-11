# Numpy library is used for creating and manipulating arrays

import numpy as np  # importing numpy library

a = np.array([1,2,3,4,5,6])
print(a)
#OUTPUT-
"""
[1 2 3 4 5 6]
"""

# multi-dimentional array
a = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
print(a)
print(a.shape) # returms the shape of the array
#OUTPUT 
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
(3, 3)
"""


a = np.array([[[1,2,3],[4,5,6]],
            [[7,8,9], [10,11,12]],
              [[13,14,15], [16,17,18]],
              [[19,20,21], [22,23,24]]])
print(a)
#OUTPUT-
"""
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]

 [[13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]]]
  """

# To access an Element in an array
print(a[1])
#OUTPUT-
"""
[[ 7  8  9]
 [10 11 12]]
 """

# to access a perticular element
print(a[2][1])
print(a[2][1][2])
#OUTPUT-
"""
[16 17 18]
18
"""


import numpy as np

x= np.zeros([10,5],dtype=int)
print(x)
#OUTPUT
"""
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
 """

x= np.ones([10,5],dtype=int)
print(x)
#OUTPUT
"""
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
 """


# array of linear values
x= np.arange(10,20,2)
print(x)
#OUTPUT
"""
[10 12 14 16 18]
"""


x = np.arange(1,100)
print(x)
#OUTPUT
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72
 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96
 97 98 99]
 """


# to generate an array for evenly spaced elements
a = np.linspace(10,20,5)
print(a)
#OUTPUT -[10.  12.5 15.  17.5 20. ]


a = np.linspace(10,50,5)
print(a)
#OUTPUT- [10. 20. 30. 40. 50.]


# slicing
x = np.arange(1,100)
print(x)
print(x[25:40])
#OUTPUT-
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72
 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96
 97 98 99]
SLICED ARRAY - [26 27 28 29 30 31 32 33 34 35 36 37 38 39 40]
"""


# Array Manupulation
a = np.array([10,20,30,40,50])
b = np.array([1,2,3,4,5])

c = a+b
print(c)

c = a-b
print(c)

c = a/b
print(c)

c = a*b
print(c)

c = a*b+5
print(c)
#OUTPUT-
"""
[11 22 33 44 55]
[ 9 18 27 36 45]
[10. 10. 10. 10. 10.]
[ 10  40  90 160 250]
[ 15  45  95 165 255]
"""

a = np.array([10,20,30,40,50])
print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
#OUTPUT
"""
10
50
150
30.0
"""
