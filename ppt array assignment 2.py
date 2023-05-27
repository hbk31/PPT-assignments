#!/usr/bin/env python
# coding: utf-8

# # Q.1

# #Sort the input array nums in non-decreasing order.
# 
# Initialize a variable max_sum to 0. This variable will store the maximum sum of minimum elements.
# 
# Iterate over the sorted array starting from index 0 with a step size of 2 (i.e., 0, 2, 4, ...).
# 
# For each iteration, add nums[i] to max_sum. Since nums is sorted, nums[i] will always be one of the minimum elements in its pair.
# 
# Return the value of max_sum.
# 

# In[1]:


def array_pair_sum(nums):
    nums.sort()  # Sort the array in non-decreasing order
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum


# In[2]:


nums = [1, 4, 3, 2]
max_sum = array_pair_sum(nums)
print(max_sum)


# The code correctly outputs the maximum sum of minimum elements, which is 4 in this case.

# # Q.2

# To find the maximum number of different types of candies Alice can eat while following the doctor's advice, we need to count the number of unique candy types in the array candyType and compare it with n / 2.
# 
# Here's an algorithm to solve this problem:
# 
# Create a set unique_candies to store the unique candy types.
# 
# Iterate over each candy in candyType.
# 
# Add each candy to the unique_candies set.
# 
# Calculate the maximum number of different types of candies Alice can eat by taking the minimum of the size of unique_candies and n / 2.
# 
# Return the maximum number of different types of candies.

# In[3]:


def max_unique_candies(candyType):
    unique_candies = set()
    for candy in candyType:
        unique_candies.add(candy)
    return min(len(unique_candies), len(candyType) // 2)


# In[4]:


candyType = [1, 1, 2, 2, 3, 3]
max_types = max_unique_candies(candyType)
print(max_types)


# The code correctly outputs the maximum number of different types of candies Alice can eat, which is 3 in this case.

# # Q.3

# To find the length of the longest harmonious subsequence in an array, we can use a frequency map to count the occurrences of each number in the array. Then, we iterate through the frequency map and check if the current number and its adjacent number (either smaller or larger by 1) form a harmonious subsequence. If they do, we calculate the length of the subsequence and keep track of the maximum length encountered.
# 
# Here's an algorithm to solve this problem:
# 
# 
# Initialize an empty frequency map freq_map to count the occurrences of each number in nums.
# 
# Iterate through each number num in nums:
# 
# Increment the count of num in freq_map.
# 
# Initialize a variable max_length to 0 to store the maximum length of harmonious subsequences.
# 
# Iterate through each number num in freq_map:
# 
# If num + 1 exists in freq_map, calculate the length of the harmonious subsequence starting with num as freq_map[num] + freq_map[num + 1].
# 
# If the calculated length is greater than max_length, update max_length with the new length.
# 
# Return max_length.

# In[5]:


def findLHS(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_length = 0
    for num in freq_map:
        if num + 1 in freq_map:
            length = freq_map[num] + freq_map[num + 1]
            max_length = max(max_length, length)

    return max_length


# In[6]:


nums = [1, 3, 2, 2, 5, 2, 3, 7]
max_subsequence_length = findLHS(nums)
print(max_subsequence_length)


# #The code correctly outputs the length of the longest harmonious subsequence, which is 5 in this case.

# # Q.4

# To determine if n new flowers can be planted in a flowerbed without violating the no-adjacent-flowers rule, we can iterate through the flowerbed and check each plot's status along with its adjacent plots.
# 
# Here's an algorithm to solve this problem:
# 
# 
# Initialize a variable count to 0, which will track the number of new flowers that can be planted.
# 
# Iterate through each plot in the flowerbed:
# 
# If the current plot is empty (flowerbed[i] == 0) and both its adjacent plots are also empty (or the adjacent plot does not exist), plant a new flower in the current plot (flowerbed[i] = 1) and increment the count by 1.
# 
# Check if the count is greater than or equal to n. If it is, return True; otherwise, return False.

# In[8]:


def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
            i += 2  # Skip the next plot since it cannot have a flower
        else:
            i += 1

    return count >= n


# In[9]:


flowerbed = [1, 0, 0, 0, 1]
n = 1
can_plant = canPlaceFlowers(flowerbed, n)
print(can_plant)


# The code correctly outputs True, indicating that one new flower can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# # Q.5

# To find the maximum product of three numbers in an integer array, we need to consider the positive and negative numbers in the array. The maximum product can be achieved by multiplying the three largest positive numbers or by multiplying the two smallest negative numbers (if they exist) with the largest positive number.
# 
# Here's an algorithm to solve this problem:
# 
# 
# Sort the input array nums in non-decreasing order.
# 
# Calculate two products:
# 
# Product1: Multiply the last three elements of the sorted array nums[-1] * nums[-2] * nums[-3].
# 
# Product2: Multiply the first two elements of the sorted array with the last element nums[0] * nums[1] * nums[-1].
# 
# Return the maximum of Product1 and Product2.

# In[10]:


def maximumProduct(nums):
    nums.sort()  # Sort the array in non-decreasing order
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]
    return max(product1, product2)


# In[11]:


nums = [1, 2, 3]
max_product = maximumProduct(nums)
print(max_product)


# The code correctly outputs the maximum product of three numbers, which is 6 in this case.

# # Q.6

# To search for a target in a sorted array nums with O(log n) runtime complexity, we can utilize the binary search algorithm.
# 
# Here's an algorithm to solve this problem:
# 
# 
# Initialize two pointers, left and right, to the start and end of the array respectively.
# 
# Perform the following steps while left is less than or equal to right:
# 
# Calculate the middle index as mid = (left + right) // 2.
# 
# If nums[mid] is equal to the target, return mid as the index.
# 
# If nums[mid] is less than the target, set left = mid + 1 to search in the right half.
# 
# If nums[mid] is greater than the target, set right = mid - 1 to search in the left half.
# 
# If the target is not found after the above loop, return -1.

# In[12]:


def search(nums, target):
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

    return -1


# In[13]:


nums = [-1, 0, 3, 5, 9, 12]
target = 9
index = search(nums, target)
print(index)


# The code correctly outputs the index of the target, which is 4 in this case.

# # Q.7

# To check if an array is monotonic, we can compare adjacent elements and check if they maintain a consistent increasing or decreasing pattern. If we encounter any violation of this pattern, we can conclude that the array is not monotonic.
# 
# Here's an algorithm to solve this problem:
# 
# 
# Initialize two flags, isIncreasing and isDecreasing, to True.
# 
# Iterate through each element in the array starting from index 1:
# 
# If nums[i] is greater than nums[i-1], it violates the increasing pattern, so set isIncreasing to False.
# 
# If nums[i] is less than nums[i-1], it violates the decreasing pattern, so set isDecreasing to False.
# 
# If either isIncreasing or isDecreasing is True, return True, indicating that the array is monotonic.
# 
# If both isIncreasing and isDecreasing are False, return False, indicating that the array is not monotonic.

# In[14]:


def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            isDecreasing = False
        if nums[i] < nums[i - 1]:
            isIncreasing = False

    return isIncreasing or isDecreasing


# In[15]:


nums = [1, 2, 2, 3]
is_monotonic = isMonotonic(nums)
print(is_monotonic)


# The code correctly outputs True, indicating that the given array is monotonic.

# # Q.8

# To minimize the score of an integer array nums after applying the mentioned operation at most once for each index, we can make two observations:
# 
# 
# To minimize the score, we should try to make the maximum element as small as possible and the minimum element as large as possible.
# 
# The operation allows us to change nums[i] to nums[i] + x, where x is in the range [-k, k]. So, we can make nums[i] closer to the maximum and minimum values in the range [-k, k] to minimize the score.
# Here's an algorithm to solve this problem:
# 
# 
# Initialize min_num and max_num to positive and negative infinity, respectively.
# 
# Iterate through each number num in nums:
# 
# Update min_num with min(min_num, num).
# 
# Update max_num with max(max_num, num).
# 
# Calculate the difference between max_num and min_num, which represents the initial score.
# 
# If the initial score is already 0, return 0.
# 
# Calculate the potential minimum score by trying all possible values of x in the range [-k, k] for each element in nums.
# Initialize potential_min_score to positive infinity.
# 
# Iterate through each number num in nums:
# 
# Calculate potential_min_score as the minimum of potential_min_score and max(max_num - k, num + k) - min(min_num + k, num - k).
# 
# Return "potential_min_score."

# In[16]:


def minimumScore(nums, k):
    min_num = float('inf')
    max_num = float('-inf')

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    initial_score = max_num - min_num

    if initial_score == 0:
        return 0

    potential_min_score = float('inf')

    for num in nums:
        potential_min_score = min(potential_min_score, max(max_num - k, num + k) - min(min_num + k, num - k))

    return potential_min_score


# In[18]:


nums = [1]
k = 0
min_score = minimumScore(nums, k)
print(min_score)


# The code correctly outputs the minimum score of nums, which is 0 in this case.
