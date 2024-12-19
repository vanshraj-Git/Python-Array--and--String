import numpy as np

# 1D Array
a = np.array([1, 2, 3, 4, 5])

# 2D Array (Matrix)
b= np.array([[1, 2, 3],[4, 5, 6]])

# 1. Accessing elements
print(a[2])  
print(b[1, 2])  

# 2. Array Shape
print(b.shape)  

# 3. Adding two arrays
c = a+ np.array([10, 10, 10, 10, 10]) 

# 4. Multiplying arrays element-wise
d = a * 2  

# 5. Transpose of a matrix
print(b.T)  
print(a)
print(b)
print(c)
print(d)
