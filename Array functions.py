import array
arr = array.array('i', [10, 20, 30, 40, 50])

# 1. Accessing elements
print(arr[0]) 

# 2. Appending an element
arr.append(60)  
print(arr)

# 3. Inserting an element at a specific position
arr.insert(2, 25)  
print(arr)

# 4. Removing an element
arr.remove(25)  
print(arr)

# 5. Popping the last element
arr.pop()  
print(arr)

# 6. Finding the index of an element
print(arr.index(30)) 

# 7. Reversing the array
arr.reverse()
print(arr)
