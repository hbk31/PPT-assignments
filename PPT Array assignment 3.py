#!/usr/bin/env python
# coding: utf-8

# # Q.1

#  we can use a two-pointer approach

# In[1]:


def threeSumClosest(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    closest_sum = float('inf')  # Initialize the closest sum to positive infinity

    for i in range(n-2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:  # If we find an exact match, return the target sum
                return curr_sum
            
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum  # Update the closest sum if necessary
            
            if curr_sum < target:
                left += 1  # Move the left pointer to increase the sum
            else:
                right -= 1  # Move the right pointer to decrease the sum
    
    return closest_sum


# In this implementation, we first sort the given array nums in ascending order. Then, we iterate through the array from the beginning, considering each element as a potential first element of the triplet. For each fixed first element, we use two pointers (left and right) to find the other two elements whose sum, along with the first element, is closest to the target.
# 
# We update the closest_sum whenever we find a sum that is closer to the target than the previously recorded closest sum. Finally, we return the closest_sum after iterating through all possible combinations.

# In[2]:


nums = [-1, 2, 1, -4]
target = 1

print(threeSumClosest(nums, target))


# In this case, the closest sum to the target of 1 is 2 (-1 + 2 + 1 = 2).

# # Q.2

# To find all unique quadruplets in an array that sum up to a given target, you can follow a similar approach to the two-sum and three-sum problems

# Sort the given array nums in ascending order. This will help in finding unique solutions and optimizing the search process.
# 
# Initialize an empty list result to store the unique quadruplets.
# 
# Iterate over the array nums from index i = 0 to n - 4, where n is the length of nums.
# 
# If i > 0 and nums[i] is equal to nums[i-1], continue to the next iteration to avoid duplicates.
# Iterate over the array from index j = i + 1 to n - 3.
# 
# If j > i + 1 and nums[j] is equal to nums[j-1], continue to the next iteration to avoid duplicates.
# Initialize two pointers left and right pointing to j + 1 and n - 1, respectively.
# 
# While left < right, perform the following steps:
# Calculate the sum total = nums[i] + nums[j] + nums[left] + nums[right].
# 
# If total is less than target, increment left by 1.
# 
# If total is greater than target, decrement right by 1.
# 
# If total is equal to target, add the quadruplet [nums[i], nums[j], nums[left], nums[right]] to the result.
# 
# Increment left by 1 and decrement right by 1.
# 
# Skip any duplicate values for left and right.
# 
# Return the result list containing all unique quadruplets.

# In[3]:


def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

    return result


# In[4]:


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))


# The algorithm finds all unique quadruplets in the nums array that sum up to the target value. The output contains the three unique quadruplets satisfying the given conditions.

# # Q.3

# To find the next permutation of an array nums, we can follow these steps:
# 
# Start from the rightmost element of nums and find the first pair of adjacent elements nums[i] and nums[i-1] where nums[i] > nums[i-1]. This means we have found a suffix that is not in descending order.
# 
# If no such pair is found, it means the entire array is in descending order, and we cannot generate the next permutation. In this case, we reverse the array to obtain the lowest possible order.
# 
# If we found the pair in step 1, we need to find the next greater element than nums[i-1] within the suffix to its right. We swap this element with nums[i-1].
# 
# Finally, we reverse the suffix starting from index i onwards to get the next lexicographically greater permutation.

# In[5]:


def nextPermutation(nums):
    # Step 1: Find the first pair of adjacent elements in descending order
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    # Step 2: Reverse the entire array if no pair is found
    if i == 0:
        nums.reverse()
        return

    # Step 3: Find the next greater element and swap it with nums[i-1]
    j = len(nums) - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # Step 4: Reverse the suffix
    nums[i:] = reversed(nums[i:])

# Example usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]


# In the given example, the initial array is [1, 2, 3]. Following the steps outlined above, we find that the next permutation is [1, 3, 2].

# # Q.4

# To solve this problem with O(log n) runtime complexity, we can use the binary search algorithm. Here's the algorithm to find the index of the target value or the index where it would be inserted in order:
# 
# Set two pointers, left and right, to the start and end of the array, respectively.
# 
# While left <= right, do:
# a. Calculate the middle index as mid = (left + right) / 2.
# 
# b. If nums[mid] is equal to the target value, return mid.
# 
# c. If nums[mid] is less than the target value, update left = mid + 1.
# 
# d. If nums[mid] is greater than the target value, update right = mid - 1.
# 
# If the target value is not found in the array, return the value of left, which represents the index where it would be inserted in order.

# In[6]:


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# In[7]:


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))


# In this case, the target value is found at index 2 in the array nums, so the output is 2.

# # Q.5

# To increment a large integer represented as an integer array by one, we need to simulate the process of adding one to the integer. We start from the least significant digit (the rightmost digit) and proceed towards the most significant digit (the leftmost digit).
# 
# 
# Here's the algorithm to increment the large integer:
# 
# 
# Initialize a carry variable to 1. This represents the value to be added to the current digit.
# 
# Traverse the array from right to left:
# Add the carry to the current digit.
# 
# If the sum of the current digit and the carry is less than 10, update the current digit with the sum and set the carry to 0.
# 
# If the sum is equal to 10, set the current digit to 0 and keep the carry as 1.
# 
# Repeat this process for each digit in the array.
# 
# After traversing the entire array, check if the carry is still 1. If it is, it means there was a carry beyond the most significant digit. In this case, append a new digit 1 to the beginning of the array.
# 
# Return the updated array.

# In[8]:


def plusOne(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] < 10:
            carry = 0
            break
        digits[i] = 0
    
    if carry == 1:
        digits.insert(0, 1)
    
    return digits


# In[9]:


digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]


# The resulting array is indeed [1, 2, 4], as expected.

# # Q.6

# To find the single number in the given array, we can use the XOR operation. XORing a number with itself results in 0, so if we XOR all the numbers in the array, the duplicate numbers will cancel out, and we will be left with the single number.
# 
# Here's the algorithm to solve the problem:
# 
# Initialize a variable result to 0.
# 
# Iterate through each number num in the array nums.
# 
# XOR num with result and store the result back in result.
# 
# At the end of the iteration, result will contain the single number.

# In[10]:


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test the function
nums = [2, 2, 1]
print(singleNumber(nums))


# The function singleNumber takes the input array nums and returns the single number that appears only once in the array. In the given example, the single number is 1, and the function correctly returns the output 1.

# # Q.7

# we can iterate over the given range [lower, upper] and check for missing numbers. Whenever we find a missing number, we start a new range. Here's the step-by-step approach:
# 
# Initialize an empty list result to store the ranges.
# 
# Iterate over the range from lower to upper (inclusive).
# 
# For each number num in the range, check if it exists in the nums array. If it doesn't exist, it's a missing number.
# 
# If num is a missing number, start a new range. Initialize start as num and increment num until we find the next number that is not missing or until we reach upper. Let's call this number end.
# 
# Append the range [start, end] to the result list.
# 
# Return the result list as the final output.

# In[14]:


def findMissingRanges(nums, lower, upper):
    result = []
    start = lower
    
    for num in nums:
        if num > upper:
            break
        
        if start < num:
            result.append([start, num - 1])
        
        start = num + 1
    
    if start <= upper:
        result.append([start, upper])
    
    return result


# In[15]:


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))


# The output matches the expected result, and it covers all the missing numbers with the shortest possible ranges.

# # Q.8

# To determine if a person could attend all meetings, we need to check if there are any overlapping intervals in the given array. If there are overlapping intervals, it means that the person cannot attend all the meetings because they would be double-booked.
# 
# Here's a step-by-step algorithm to solve this problem:
# 
# Sort the intervals array based on the start time of each interval. This step ensures that the intervals are ordered chronologically.
# 
# Iterate through the sorted intervals array, starting from the second interval (index 1).
# 
# For each interval, compare its start time with the end time of the previous interval. If the start time of the current interval is less than or equal to the end time of the previous interval, there is an overlap.
# 
# If an overlap is found, return false, indicating that the person cannot attend all meetings.
# 
# If the loop completes without finding any overlaps, return true, indicating that the person can attend all meetings.

# In[16]:


def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True


# In[17]:


intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))


# The output indicates that a person cannot attend all meetings because there is an overlap between the intervals [0, 30] and [15, 20].
