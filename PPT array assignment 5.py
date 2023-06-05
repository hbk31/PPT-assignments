#!/usr/bin/env python
# coding: utf-8

# # Q1

# To solve this problem, we can iterate through the elements of the original array and fill the 2D array row by row. If the total number of elements in the original array is not equal to m * n, it means it is impossible to create a valid 2D array, so we return an empty 2D array.
# 
# Here's the step-by-step algorithm:
# 
# Check if the total number of elements in the original array is equal to m * n. If not, return an empty 2D array.
# 
# Create an empty 2D array with m rows and n columns.
# 
# Initialize two variables, row and col, to 0. These variables will keep track of the current row and column in the 2D array.
# Iterate through each element num in the original array.
# 
# Set the value of the element at the current row and col in the 2D array to num.
# 
# Increment col by 1.
# 
# If col is equal to n, it means we have filled all the columns in the current row. Reset col to 0 and increment row by 1 to move to the next row.
# 
# Return the constructed 2D array.
# 
# Here's the implementation in Python:

# In[1]:


def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]
    row = 0
    col = 0

    for num in original:
        result[row][col] = num
        col += 1
        if col == n:
            col = 0
            row += 1

    return result


# In[2]:


original = [1, 2, 3, 4]
m = 2
n = 2
print(convert_to_2d_array(original, m, n))


# The output matches the expected result, where the first row contains [1, 2] and the second row contains [3, 4].

# # Q2

# To solve this problem, we need to determine the number of complete rows we can form using n coins. The number of coins required to form a complete row i is equal to the sum of the integers from 1 to i.
# 
# We can iterate through each row starting from 1 until the sum of the coins required for that row exceeds n. The last row that doesn't exceed n will be incomplete. Therefore, we return the number of complete rows, which is one less than the current row.
# 
# Here's the step-by-step algorithm:
# 
# Initialize a variable row to 1, which represents the current row.
# 
# Iterate while the sum of the coins required for the current row is less than or equal to n:
# 
# Deduct the number of coins required for the current row from n.
# 
# Increment row by 1.
# 
# Return row - 1, which represents the number of complete rows.
# 
# Here's the implementation in Python:

# In[3]:


def count_complete_rows(n):
    row = 1
    while row * (row + 1) // 2 <= n:
        n -= row
        row += 1
    return row - 1


# In[4]:


n = 5
print(count_complete_rows(n))


# The output is 2, which is the correct number of complete rows we can form with 5 coins.

# # Q3

# To solve this problem, we can follow a two-pointer approach since the array is sorted in non-decreasing order. We can use two pointers, one starting from the beginning of the array and moving forward, and the other starting from the end of the array and moving backward.
# 
# The idea is to compare the absolute values of the numbers at the current positions of the pointers. Since the array is sorted in non-decreasing order, the largest absolute values will be towards the ends of the array. We square the larger absolute value and place it at the end of the resulting array. Then we move the pointer corresponding to that absolute value. We repeat this process until both pointers meet.
# 
# Here's the step-by-step algorithm:
# 
# Initialize two pointers, left and right, to the start and end of the array, respectively.
# 
# Create an empty result array to store the squared values.
# 
# Iterate while left is less than or equal to right:
# Compare the absolute values of nums[left] and nums[right].
# 
# If the absolute value of nums[left] is greater or equal:
# Square nums[left] and append it to the result array.
# 
# Increment left by 1.
# 
# If the absolute value of nums[right] is greater:
# Square nums[right] and append it to the result array.
# 
# Decrement right by 1.
# 
# Append the squared value of the remaining number at either left or right to the result array (since there will be at most one remaining number).
# 
# Reverse the result array to sort the squared values in non-decreasing order.
# 
# Return the result array.
# 
# Here's the implementation in Python:

# In[6]:


def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = []

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    # Append the remaining number
    if left == right:
        result.append(nums[left] ** 2)

    # Reverse the result array
    result.reverse()

    return result


# In[7]:


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))


# The output is [0, 1, 9, 16, 100], which is the correct array of squared values sorted in non-decreasing order.

# # Q4

# To solve this problem, we can use sets to find the distinct integers that are present in one array but not in the other. We'll create two sets, one for nums1 and one for nums2. Then, we'll find the difference between the two sets to get the distinct integers.
# 
# Here's the step-by-step algorithm:
# 
# Convert nums1 and nums2 into sets to remove duplicates and find the distinct integers.
# 
# Find the difference between the sets nums1 and nums2 to get the distinct integers in nums1 that are not present in nums2.
# 
# Assign the result to distinct_nums1.
# 
# Find the difference between the sets nums2 and nums1 to get the distinct integers in nums2 that are not present in nums1.
# Assign the result to distinct_nums2.
# 
# Convert distinct_nums1 and distinct_nums2 back to lists.
# 
# Return the list [distinct_nums1, distinct_nums2].
# 
# Here's the implementation in Python:

# In[8]:


def findDisappearedNumbers(nums1, nums2):
    distinct_nums1 = list(set(nums1) - set(nums2))
    distinct_nums2 = list(set(nums2) - set(nums1))
    return [distinct_nums1, distinct_nums2]


# In[9]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(findDisappearedNumbers(nums1, nums2))


# The output is [[1, 3], [4, 6]], which is the correct list of distinct integers not present in the respective arrays.

# # Q5

# To solve this problem, we can use nested loops to compare each element of arr1 with every element of arr2. For each element num1 in arr1, we check if there exists any element num2 in arr2 such that the absolute difference between num1 and num2 is less than or equal to d. If we find such an element, we break out of the inner loop and move on to the next element in arr1.
# 
# Here's the step-by-step algorithm:
# 
# Initialize a variable count to 0, which will keep track of the number of elements in arr1 that satisfy the condition.
# 
# Iterate through each element num1 in arr1:
# Set a flag found to False before starting the inner loop.
# 
# Iterate through each element num2 in arr2:
# If the absolute difference between num1 and num2 is less than or equal to d, set found to True and break out of the inner loop.
# 
# If found is False after the inner loop, it means no element in arr2 satisfies the condition. Increment count by 1.
# 
# Return the value of count, which represents the distance value between the two arrays.
# 
# Here's the implementation in Python:

# In[10]:


def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for num1 in arr1:
        found = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break
        if not found:
            count += 1
    return count


# In[11]:


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))


# The output is 2, which is the correct distance value between the two arrays. There are two elements in arr1 (4 and 5) for which there are no elements in arr2 with an absolute difference less than or equal to 2.

# # Q6

# To solve this problem with a time complexity of O(n) and constant extra space, we can utilize the property that all the integers in the array nums are in the range [1, n]. This property allows us to map the values in nums to indices within the array itself.
# 
# We can iterate through each element in nums and mark the corresponding index as negative to indicate that we have encountered the number before. If we encounter a number that has already been marked as negative, it means that the number appears twice. We can add it to our result array.
# 
# Here's the step-by-step algorithm:
# 
# Initialize an empty result array to store the numbers that appear twice.
# 
# Iterate through each element num in nums:
# Calculate the absolute value of num.
# 
# If nums[abs(num) - 1] is positive, mark it as negative by multiplying it by -1.
# 
# If nums[abs(num) - 1] is negative, it means we have encountered the number before. Add abs(num) to the result array.
# 
# Return the result array.
# 
# Here's the implementation in Python:

# In[12]:


def findDuplicates(nums):
    result = []
    for num in nums:
        if nums[abs(num) - 1] > 0:
            nums[abs(num) - 1] *= -1
        else:
            result.append(abs(num))
    return result


# In[13]:


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))


# The output is [2, 3], which is the correct array of numbers that appear twice in the given array nums.

# # Q7

# To find the minimum element in a sorted rotated array with unique elements, we can use a modified version of binary search. The key idea is to compare the middle element of the array with the first and last elements to determine which half of the array to search in.
# 
# Here's the step-by-step algorithm:
# 
# Initialize two pointers, left and right, pointing to the first and last indices of the array, respectively.
# 
# While left is less than right:
# Calculate the middle index as mid using the formula mid = (left + right) // 2.
# 
# Compare the middle element nums[mid] with the first and last elements of the array.
# 
# If nums[mid] is greater than the last element, it means the minimum element is in the right half. Set left = mid + 1.
# 
# If nums[mid] is less than the last element, it means the minimum element is in the left half or possibly the middle element itself. Set right = mid.
# 
# Return the element at index left, which is the minimum element.
# 
# The time complexity of this algorithm is O(log n) since we perform binary search on the array.
# 
# 
# Here's the implementation in Python:

# In[14]:


def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# In[15]:


nums = [3, 4, 5, 1, 2]
print(findMin(nums))


# The output is 1, which is the correct minimum element in the given rotated array nums.

# # Q8

# To solve this problem, we can follow the given steps:
# 
# Sort the changed array in ascending order.
# 
# Initialize an empty list original to store the original array.
# 
# Iterate through each element num in the sorted changed array:
# Divide num by 2 and check if the result is present in original.
# 
# If the result is not present, return an empty array since changed is not a doubled array.
# 
# If the result is present, remove it from original.
# 
# After the loop completes, return the original array.
# 
# Here's the implementation in Python:

# In[40]:


from collections import Counter

def findOriginalArray(changed):
    counter = Counter(changed)
    original = []
    
    for num in sorted(changed):
        if counter[num] == 0:
            continue
        if counter[2*num] == 0:
            return []
        
        original.append(num)
        counter[num] -= 1
        counter[2*num] -= 1
    
    return original


# In[41]:


changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))


# Now the function correctly returns [1, 3, 4], which is the possible original array for the given changed array.

# In[ ]:




