#!/usr/bin/env python
# coding: utf-8

# # Q.1

# There are several approaches you can use to reconstruct the permutation `perm` from the given string `s`. Here are a few possible approaches:
# 
# Approach 1: Greedy Algorithm
# 1. Initialize an empty list `perm` to store the reconstructed permutation.
# 2. Initialize two variables `low` and `high` to keep track of the lowest and highest available numbers, respectively. Set `low = 0` and `high = len(s)`.
# 3. Iterate over each character `c` in `s`:
#    - If `c` is 'I', append `low` to `perm` and increment `low` by 1.
#    - If `c` is 'D', append `high` to `perm` and decrement `high` by 1.
# 4. Append the remaining value of `low` or `high` to `perm`.
# 5. Return the reconstructed permutation `perm`.
# 
# Approach 2: Stack
# 1. Initialize an empty stack `stack` to store the reconstructed permutation.
# 2. Initialize a variable `n` to the length of `s` and a variable `count` to 0.
# 3. Iterate over each character `c` in `s`:
#    - If `c` is 'I', push `count` to the `stack` and increment `count` by 1.
#    - If `c` is 'D', push `count` to the `stack` and increment `count` by 1. Then, while the stack is not empty, pop the top element and append it to the reconstructed permutation `perm`.
# 4. Push the remaining value of `count` to the `stack`.
# 5. While the stack is not empty, pop the top element and append it to `perm`.
# 6. Return the reconstructed permutation `perm`.
# 
# These are two possible approaches to reconstruct the permutation `perm` from the given string `s`. Both approaches should provide valid permutations, and the specific permutation returned may vary depending on the implementation.

# In[5]:


def reconstruct_permutation(s):
    n = len(s)
    perm = []
    low = 0
    high = n

    for c in s:
        if c == 'I':
            perm.append(low)
            low += 1
        elif c == 'D':
            perm.append(high)
            high -= 1
    
    # Append the remaining value of low or high
    perm.append(low)

    return perm


# # Q.2

# To solve this problem efficiently with a time complexity of O(log(m * n)), we can use a modified binary search algorithm. Since the matrix has the properties of each row being sorted in non-decreasing order and the first integer of each row being greater than the last integer of the previous row, we can treat the 2D matrix as a 1D sorted array and perform a binary search on it.
# 
# Here's the Python code that implements this approach:

# In[7]:


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# In this code, we use the variables left and right to define the range of the search. Initially, left is set to 0 and right is set to the index of the last element in the matrix (rows * cols - 1). We continuously update the range by comparing the middle element (mid_element) with the target value.
# 
# If the middle element is equal to the target, we return True. If it is less than the target, we update left to mid + 1 to search in the upper half of the range. If it is greater than the target, we update right to mid - 1 to search in the lower half of the range. We repeat this process until the range is exhausted (left > right), indicating that the target is not present in the matrix.
# 
# Note that we handle the edge case where the matrix is empty (not matrix or not matrix[0]) by returning False.
# 
# Using this algorithm, we can determine whether the target value is present in the matrix efficiently with a time complexity of O(log(m * n)).

# # Q.3

# To determine whether an array arr is a valid mountain array, we need to check if it satisfies the conditions mentioned in the problem statement. Here's the Python code to solve this problem:

# In[8]:


def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    # Check the increasing part
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # If the peak is at the start or end, it's not a valid mountain array
    if i == 0 or i == n - 1:
        return False

    # Check the decreasing part
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # If the pointer doesn't reach the end, it's not a valid mountain array
    return i == n - 1


# In this code, we start by checking the length of the array arr. If it is less than 3, we directly return False since a valid mountain array requires at least three elements.
# 
# Next, we initialize a pointer i to 0 and start traversing the array to find the increasing part. We continue incrementing i until either we reach the end of the array or the elements stop increasing (arr[i] >= arr[i + 1]).
# 
# After finding the increasing part, we check if the pointer i is at the start or end of the array. If it is, it means the array either starts with the increasing part or ends with it, and thus it cannot be a valid mountain array. In such cases, we return False.
# 
# If the pointer i is neither at the start nor at the end, we continue checking the remaining part of the array to find the decreasing part. Similar to before, we increment i until either we reach the end of the array or the elements stop decreasing (arr[i] <= arr[i + 1]).
# 
# Finally, if the pointer i reaches the end of the array, it means we have successfully traversed both the increasing and decreasing parts, satisfying the conditions of a valid mountain array. In this case, we return True. Otherwise, we return False.
# 
# Using this approach, we can determine whether an array is a valid mountain array or not.

# # Q.4

# To find the maximum length of a contiguous subarray with an equal number of 0s and 1s in a binary array nums, we can use a technique called the "prefix sum" approach. Here's the Python code to solve this problem:

# In[9]:


def findMaxLength(nums):
    count = 0
    max_length = 0
    count_map = {0: -1}  # Map to store the count at each index

    for i in range(len(nums)):
        # Increment count for 1, decrement count for 0
        count += 1 if nums[i] == 1 else -1

        if count in count_map:
            # Calculate the length of the subarray
            length = i - count_map[count]
            max_length = max(max_length, length)
        else:
            # Store the count at the first occurrence
            count_map[count] = i

    return max_length


# In this code, we initialize count and max_length to 0. The variable count keeps track of the difference between the number of 0s and 1s encountered so far. We use a dictionary count_map to store the count at each index. We initialize it with an entry 0: -1 to handle the case when the balanced subarray starts from the beginning.
# 
# We iterate through the array nums, incrementing count by 1 if the element is 1 and decrementing it by 1 if the element is 0. If the current count is already present in the count_map, it means we have encountered an equal number of 0s and 1s between the current index and the index stored in the count_map. We calculate the length of the subarray by subtracting the current index from the stored index and update max_length if necessary.
# 
# If the current count is not present in the count_map, we store the current index as the first occurrence of that count.
# 
# Finally, we return max_length, which represents the maximum length of a contiguous subarray with an equal number of 0s and 1s.
# 
# This algorithm has a time complexity of O(n), where n is the length of the binary array nums.

# # Q.5

# To find the minimum product sum by rearranging the order of elements in nums1, we can sort both nums1 and nums2 in different orders and calculate the product sum for each arrangement. The minimum product sum will be the smallest one among all the calculated product sums.

# In[10]:


def minProductSum(nums1, nums2):
    nums1.sort()  # Sort nums1 in ascending order
    nums2.sort(reverse=True)  # Sort nums2 in descending order

    n = len(nums1)
    product_sum = sum(nums1[i] * nums2[i] for i in range(n))

    return product_sum


# In this code, we first sort nums1 in ascending order using the sort() function. Then, we sort nums2 in descending order by passing reverse=True as an argument to the sort() function.
# 
# After sorting both arrays, we iterate over the indices i from 0 to n-1 and calculate the product sum by multiplying nums1[i] with nums2[i] for each index. We use a generator expression and the sum() function to calculate the sum of these products.
# 
# Finally, we return the calculated product_sum, which represents the minimum product sum among all possible rearrangements of nums1.
# 
# This algorithm has a time complexity of O(n log n), where n is the length of the input arrays nums1 and nums2, due to the sorting operation.

# # Q.6

# To solve this problem, we can iterate over the elements in the changed array and check if each element's value is exactly half of some other element's value. If so, we can construct the original array by dividing each element's value by 2. We also need to account for the possibility of duplicate values in the original array.

# In[12]:


def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # The length of changed must be even for it to be a doubled array

    freq_map = {}  # Dictionary to store the frequency of each element

    for num in changed:
        freq_map[num] = freq_map.get(num, 0) + 1

    original = []  # List to store the original array

    for num in sorted(changed):
        if freq_map.get(num, 0) == 0:
            continue

        if freq_map.get(num * 2, 0) == 0:
            return []  # changed is not a doubled array

        original.append(num)
        freq_map[num] -= 1
        freq_map[num * 2] -= 1

    return original


# In this code, we first check if the length of the changed array is odd. If it is, we return an empty array because a doubled array must have an even length.
# 
# We then create a frequency map called freq_map to store the frequency of each element in the changed array.
# 
# Next, we iterate over the elements in the changed array in sorted order. For each element num, we check if its frequency is greater than 0 in the freq_map. If it is, we also check if num * 2 has a frequency greater than 0 in the freq_map. If both conditions are satisfied, we add num to the original array, decrement the frequencies of num and num * 2 in the freq_map, and continue to the next element.
# 
# If we successfully process all the elements in the changed array, we return the original array. Otherwise, if at any point the conditions for a doubled array are not met, we return an empty array.
# 
# Please note that the original array may contain duplicate values, and the order of elements in the original array can be in any order.
# 
# Using this approach, we can determine if the changed array is a doubled array and construct the corresponding original array if it is valid.

# # Q.7

# To generate an n x n matrix filled with elements from 1 to n^2 in spiral order, we can use a simple iterative approach. 

# In[11]:


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]  # Initialize the matrix with zeros
    num = 1  # Current number to fill in the matrix
    top = 0  # Topmost row index
    bottom = n - 1  # Bottommost row index
    left = 0  # Leftmost column index
    right = n - 1  # Rightmost column index

    while num <= n * n:
        # Fill the top row from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill the right column from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill the bottom row from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill the left column from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


# In this code, we initialize an empty matrix of size n x n with all elements set to 0. We also initialize the variables num, top, bottom, left, and right to keep track of the current number to fill in the matrix and the indices of the top, bottom, left, and right boundaries of the spiral.
# 
# We use a while loop that continues until we have filled all the elements in the matrix. Inside the loop, we fill the top row from left to right, the right column from top to bottom, the bottom row from right to left, and the left column from bottom to top. After filling each segment, we update the corresponding boundary indices accordingly.
# 
# Finally, we return the filled matrix.
# 
# By following this approach, we can generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

# # Q.8

# To perform matrix multiplication on two sparse matrices mat1 and mat2, we can utilize a sparse matrix representation and perform the multiplication based on the definition of matrix multiplication.

# In[13]:


def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    # Create a result matrix with dimensions m x n
    result = [[0] * n for _ in range(m)]

    # Convert mat2 to a column-wise dictionary representation
    mat2_dict = {}
    for j in range(n):
        mat2_dict[j] = {}
        for i in range(k):
            if mat2[i][j] != 0:
                mat2_dict[j][i] = mat2[i][j]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for idx, val in mat1[i].items():
                if idx in mat2_dict[j]:
                    result[i][j] += val * mat2_dict[j][idx]

    return result


# In this code, we first obtain the dimensions of the input matrices: m (number of rows in mat1), k (number of columns in mat1 and rows in mat2), and n (number of columns in mat2).
# 
# Next, we create an empty result matrix of dimensions m x n filled with zeros.
# 
# To optimize the multiplication process, we convert mat2 into a column-wise dictionary representation called mat2_dict. Each column index j in mat2_dict maps to a dictionary containing the non-zero values and their corresponding row indices in that column.
# 
# We then perform the matrix multiplication by iterating over the rows and columns of the result matrix. For each element result[i][j], we iterate over the non-zero elements in the i-th row of mat1 (stored as a dictionary mat1[i]). If the corresponding column index (idx) in mat1[i] is present in mat2_dict[j], we perform the multiplication and accumulate the result in result[i][j].
# 
# Finally, we return the resulting matrix.
# 
# Using this approach, we can efficiently perform matrix multiplication on sparse matrices mat1 and mat2.

# In[ ]:




