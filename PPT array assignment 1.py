#!/usr/bin/env python
# coding: utf-8

# # Q.1

# #To find the indices of the two numbers in the given array that add up to the target value, you can use a two-pointer approach. Here's the solution in Python:

# In[25]:


def twoSum(nums, target):
    complements = {}
    for i, num in enumerate(nums):
        if num in complements:
            return [complements[num], i]
        else:
            complements[target - num] = i
    return []


# In[26]:


nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)


# # Q.2

# #To solve this problem, you can use the two-pointer technique to remove occurrences of the given value in-place.

# In[27]:


def removeElement(nums, val):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j


# In[28]:



nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print("k =", k)
print("nums =", nums[:k] + ['_'] * (len(nums) - k))


# #In the above code, we maintain two pointers i and j. The pointer i iterates through the array to find elements that are not equal to the given val. When a non-val element is found, it is placed at the j-th position in the array, and j is incremented. This ensures that the non-val elements are placed at the beginning of the array. Finally, we return j as the number of elements in the updated array

# # Q. 3

# In[29]:


#To find the index where the target value would be inserted in a sorted array of distinct integers, you can use a binary search algorithm.


# In[31]:


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


# In[32]:


nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)


# #In the code above, we initialize the left pointer to 0 and the right pointer to the last index of the array. We then perform a binary search by repeatedly dividing the search space in half. If the middle element is equal to the target, we return its index. If the middle element is greater than the target, we search the left half of the array. If the middle element is less than the target, we search the right half of the array. The search continues until the left pointer is greater than the right pointer, indicating that the target is not found. In this case, we return the left pointer as the index where the target would be inserted. The time complexity of this algorithm is O(log n) since each iteration reduces the search space by half.

# # Q.4

# #To increment a large integer represented as an array of digits by one, you can perform a simple addition operation while considering carry-over.

# In[34]:


def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits


# In[35]:


digits = [1, 2, 3]
result = plusOne(digits)
print(result)


# #In the code above, we start by initializing a carry variable with a value of 1. We then iterate through the digits array in reverse order, starting from the least significant digit. We add the carry value to the current digit and check if it becomes 10. If it does, we set the digit to 0 and propagate the carry by setting it to 1. If the current digit does not become 10, we break out of the loop. Finally, we check if there is still a carry remaining after iterating all digits. If there is, we insert it at the beginning of the array. The resulting array represents the incremented large integer.

# # Q.5

# #To merge two sorted arrays nums1 and nums2 into nums1 in a non-decreasing order, you can utilize a two-pointer approach. Since nums1 has enough space to accommodate both arrays, you can start from the end of both arrays and compare the elements, placing the larger element at the end of nums1

# In[36]:


def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    return nums1


# In[37]:


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


# In[38]:


result = merge(nums1, m, nums2, n)
print(result)


# #In the code above, we start by initializing three pointers: p1 pointing to the last element of nums1, p2 pointing to the last element of nums2, and p pointing to the end of the merged array nums1. We then compare the elements at p1 and p2, and place the larger element at p in nums1. We decrement the corresponding pointers (p1, p2, and p) accordingly. We repeat this process until we have processed all elements from either nums1 or nums2. Finally, if there are any remaining elements in nums2, we copy them to the beginning of nums1. The resulting nums1 array will contain the merged and sorted elements.

# # Q.6

# #To determine if any value appears at least twice in an integer array, you can iterate through the array and keep track of the seen elements using a set. If an element is already present in the set, it means it has appeared before, indicating the presence of a duplicate.

# In[39]:


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# In[40]:


# Example usage
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)


# #In the code above, we initialize an empty set called seen. We then iterate through each element in nums. For each element, we check if it is already present in the seen set. If it is, we return True indicating the presence of a duplicate. Otherwise, we add the element to the seen set. If we complete the loop without finding any duplicates, we return False. The time complexity of this solution is O(n) since we iterate through the array once and perform constant-time operations for each element.

# # Q.7

# #To move all zeroes to the end of an integer array while maintaining the relative order of the nonzero elements, you can utilize a two-pointer approach. One pointer keeps track of the position to insert the next nonzero element, and the other pointer scans the array for nonzero elements.

# In[41]:


def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums


# In[42]:


nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)


# #In the code above, we initialize the insert_pos pointer to keep track of the position to insert the next nonzero element. We then iterate through each element in nums. If the element is nonzero, we place it at the insert_pos position and increment insert_pos by 1. After processing all nonzero elements, we fill the remaining positions from insert_pos to the end of the array with zeroes. The resulting nums array will have all zeroes moved to the end while maintaining the relative order of the nonzero elements.

# # Q.8

# #To find the number that occurs twice and the number that is missing in the given integer array nums, you can utilize a set to keep track of the seen numbers. By iterating through nums, you can identify the repeated number and calculate the expected sum of the numbers from 1 to n to determine the missing number

# In[46]:


def findErrorNums(nums):
    n = len(nums)
    seen = set()
    duplicate = -1

    for num in nums:
        if num in seen:
            duplicate = num
            break
        seen.add(num)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum + duplicate

    return [duplicate, missing]


# In[47]:


nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)


# #In the code above, we initialize a set called seen to keep track of the seen numbers. We iterate through nums and check if each number is already present in the set. If it is, we have found the duplicate number and store it in the variable duplicate. After finding the duplicate, we calculate the expected sum of the numbers from 1 to n using the formula n * (n + 1) // 2. We then calculate the actual sum of nums. By subtracting the actual sum from the expected sum and adding the duplicate number, we obtain the missing number and store it in the variable missing. Finally, we return the array [duplicate, missing], which represents the number that occurs twice and the number that is missing in the set

# In[ ]:




