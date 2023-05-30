#!/usr/bin/env python
# coding: utf-8

# # Q.1

# To find the integers that appeared in all three arrays, you can use a simple approach. Since the arrays are sorted in strictly increasing order, you can iterate through the arrays simultaneously using three pointers, comparing the elements at each pointer.

# In[1]:


def commonElements(arr1, arr2, arr3):
    result = []  # to store the common elements
    
    # Initialize three pointers for each array
    i = j = k = 0
    
    # Iterate until one of the arrays is exhausted
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])  # found a common element
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return result


# In[2]:


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

print(commonElements(arr1, arr2, arr3))


# The function returns the sorted array containing only the integers that appeared in all three input arrays.

# # Q.2

# To solve this problem, we can iterate through each array and keep track of the distinct elements using sets. Here's the step-by-step approach to finding the distinct integers in nums1 and nums2 that are not present in the other array:
# 
# Initialize two empty sets, set1 and set2, to store the distinct elements of nums1 and nums2, respectively.
# 
# Iterate through nums1 and add each element to set1.
# 
# Iterate through nums2 and add each element to set2.
# 
# Create two empty lists, answer1 and answer2, to store the distinct integers not present in the other array.
# 
# Iterate through nums1 and check if each element is not present in set2. If it is not present, add it to answer1.
# 
# Iterate through nums2 and check if each element is not present in set1. If it is not present, add it to answer2.
# 
# Return a list [answer1, answer2] as the final result.

# In[3]:


def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    answer1 = [num for num in nums1 if num not in set2]
    answer2 = [num for num in nums2 if num not in set1]
    
    return [answer1, answer2]


# In[4]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(findDisappearedNumbers(nums1, nums2))


# The output matches the expected result, and it returns a list with two sublists. The first sublist contains the distinct integers in nums1 that are not present in nums2, and the second sublist contains the distinct integers in nums2 that are not present in nums1.

# # Q.3

# To obtain the transpose of a matrix, we need to flip the matrix over its main diagonal, switching the row and column indices. Here's a Python function that achieves this:

# In[5]:


def transpose(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with flipped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# In[6]:


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)


# The resulting matrix is the transpose of the input matrix. Each row in the input matrix becomes a column in the transposed matrix, and vice versa.

# # Q.4

# To maximize the sum of the minimum values in each pair, we should pair the smallest elements with the next smallest elements in the array. This way, we ensure that the larger elements are available for pairing with other larger elements.
# 
# Sort the given array nums in ascending order.
# 
# Initialize a variable max_sum to 0.
# 
# Iterate over the sorted array nums with a step size of 2 (since we are pairing elements).
# 
# For each iteration, add the minimum value of the current pair to max_sum.
# 
# After the iteration, max_sum will hold the maximum possible sum of the minimum values in each pair.
# Return max_sum.

# In[8]:


def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum


# Using the given example nums = [1, 4, 3, 2], the function arrayPairSum(nums) will return 4, as explained in the example.

# # Q.5

# To find the number of complete rows in the staircase, we can iterate through the rows and subtract the number of coins required for each row from the total number of coins available. We keep track of the number of rows we can fully build until we no longer have enough coins for the next row.
# Initialize a variable rows to 0 to keep track of the number of complete rows.
# 
# Initialize a variable coins to the given value of n to represent the total number of coins available.
# 
# Initialize a variable i to 1 to represent the current row number.
# 
# While coins is greater than or equal to i:
# Subtract i from coins to account for the coins used in the current row.
# 
# Increment rows by 1 to indicate a complete row.
# 
# Increment i by 1 to move to the next row.
# 
# Return the value of rows.
# 
# Here's the implementation of the above algorithm in Python:

# In[9]:


def count_complete_rows(n):
    rows = 0
    coins = n
    i = 1
    
    while coins >= i:
        coins -= i
        rows += 1
        i += 1
    
    return rows


# In[10]:


n = 5
result = count_complete_rows(n)
print(result)  # Output: 2


# The output is 2, indicating that we can build 2 complete rows with 5 coins.

# # Q.6

# Initialize an empty array to store the squared values.
# 
# Iterate through each element in the given input array nums.
# 
# Calculate the square of each element and add it to the squared array.
# 
# Sort the squared array in non-decreasing order.
# 
# Return the sorted squared array.

# In[11]:


def sortedSquares(nums):
    squared = []
    for num in nums:
        squared.append(num * num)
    squared.sort()
    return squared


# In[12]:


nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)


# The function sortedSquares takes the input array nums and returns a new array containing the squares of each number sorted in non-decreasing order.

# # Q.7

# To solve this problem, we can simulate the operations and keep track of the minimum values in each dimension. The number of maximum integers in the matrix will be equal to the product of the minimum values in each dimension.
# 
# Here's the step-by-step approach to solve the problem:
# 
# Initialize minRow and minCol variables to m and n, respectively. These variables will keep track of the minimum values in each dimension.
# 
# Iterate through each operation in the ops array.
# 
# Update minRow as the minimum between minRow and ops[i][0].
# 
# Update minCol as the minimum between minCol and ops[i][1].
# 
# Calculate the number of maximum integers in the matrix by multiplying minRow and minCol.
# 
# Return the result.

# In[14]:


def maxCount(m, n, ops):
    minRow = m
    minCol = n

    for op in ops:
        minRow = min(minRow, op[0])
        minCol = min(minCol, op[1])

    return minRow * minCol


# In[15]:


m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(maxCount(m, n, ops))


# The output is 4, which is the correct answer based on the provided example.

# # Q. 8

# To rearrange the given array nums in the specified form.
# Create an empty array called result to store the rearranged elements.
# 
# Iterate over the indices i from 0 to n-1 (inclusive).
# Within each iteration:
# 
# a. Append nums[i] to result to add the corresponding x element.
# 
# b. Append nums[i+n] to result to add the corresponding y element.
# 
# Return the result array.

# In[16]:


def rearrange_array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result


# In[17]:


nums = [2, 5, 1, 3, 4, 7]
n = 3
rearranged_nums = rearrange_array(nums, n)
print(rearranged_nums)


# The function rearrange_array takes the input array nums and the value n as arguments and returns the rearranged array.
