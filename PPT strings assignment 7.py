#!/usr/bin/env python
# coding: utf-8

# # Q.1

# To determine if two strings, s and t, are isomorphic, we need to check if we can replace the characters in s with characters in t in such a way that the order of characters is preserved.
# 
# Here's an algorithm to solve the problem:
# 
# Initialize two empty dictionaries, s_to_t and t_to_s, to store the mappings between characters of s and t.
# 
# Iterate over the characters of s and t simultaneously.
# 
# For each pair of characters (char_s, char_t):
# If char_s exists in s_to_t, check if the mapped character is equal to char_t. If not, return False because the mapping would violate the uniqueness condition.
# 
# If char_t exists in t_to_s, check if the mapped character is equal to char_s. If not, return False because the mapping would violate the uniqueness condition.
# 
# If char_s and char_t are not present in the mappings, create the mappings by adding char_s as a key mapped to char_t in s_to_t, and char_t as a key mapped to char_s in t_to_s.
# 
# If the loop completes without returning False, return True because the strings are isomorphic.

# In[1]:


def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        elif char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

    return True


# In[2]:


s = "egg"
t = "add"
print(isomorphic_strings(s, t))  # Output: True


# The output is True because we can map "e" to "a" and "g" to "d" to transform s into t.

# # Q.2

# To determine if a given string num is a strobogrammatic number, we need to check if the number remains the same when rotated 180 degrees and if the rotated number is a valid strobogrammatic number.
# 
# Here's an algorithm to solve the problem:
# 
# Initialize an empty dictionary mapping to store the mappings between digits.
# 
# Add the mappings for the strobogrammatic digits: "0" maps to "0", "1" maps to "1", "6" maps to "9", "8" maps to "8", and "9" maps to "6".
# 
# Initialize two pointers, left and right, to the start and end of the string num, respectively.
# 
# While left is less than or equal to right:
# Check if num[left] is not in the map
# ping dictionary or if num[right] is not in the mapping dictionary. If either condition is true, return False because the digit is not strobogrammatic.
# 
# Check if the mapping of num[left] in mapping is equal to num[right]. If not, return False because the digits are not strobogrammatic.
# 
# Increment left and decrement right.
# 
# If the loop completes without returning False, return True because the number is strobogrammatic.

# In[3]:


def is_strobogrammatic(num):
    mapping = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in mapping or num[right] not in mapping:
            return False

        if mapping[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True


# In[4]:


num = "69"
print(is_strobogrammatic(num))  # Output: True


# The output is True because "69" remains the same when rotated 180 degrees, making it a strobogrammatic number.`

# # Q.3

# To solve the problem of adding two non-negative integers represented as strings, num1 and num2, without converting them to integers directly or using any built-in library for handling large integers, we can follow a simple algorithm that simulates the addition process.
# 
# Here's an algorithm to solve the problem:
# 
# Initialize an empty string result to store the sum of the two numbers.
# 
# Initialize two pointers, i and j, to the end of num1 and num2, respectively.
# 
# Initialize a carry variable carry to 0.
# 
# While i or j is greater than or equal to 0:
# Initialize x to the digit at index i of num1 if i is greater than or equal to 0; otherwise, set x to 0.
# 
# Initialize y to the digit at index j of num2 if j is greater than or equal to 0; otherwise, set y to 0.
# 
# Calculate the sum curr_sum by adding x, y, and carry.
# 
# Append the least significant digit of curr_sum (i.e., curr_sum % 10) to the beginning of result.
# 
# Update the carry by setting carry to curr_sum // 10.
# 
# Decrement i and j by 1.
# 
# If the carry is greater than 0, append it to the beginning of result.
# 
# Return the final result string.

# In[5]:


def add_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        curr_sum = x + y + carry
        result = str(curr_sum % 10) + result
        carry = curr_sum // 10
        i -= 1
        j -= 1

    if carry > 0:
        result = str(carry) + result

    return result


# In[6]:


num1 = "11"
num2 = "123"
print(add_strings(num1, num2))  # Output: "134"


# The output is "134" because the sum of 11 and 123 is 134.

# # Q.4

# To reverse the order of characters in each word within a sentence while preserving whitespace and the initial word order, we can follow a simple algorithmic approach.
# 
# Here's an algorithm to solve the problem:
# 
# Split the input string s into a list of words using whitespace as the delimiter. Let's call this list words.
# Initialize an empty list reversed_words to store the reversed words.
# Iterate over each word in words.
# Reverse the characters in the current word and append it to reversed_words.
# Join the words in reversed_words into a single string using whitespace as the delimiter. Let's call this string result.
# Return result.

# In[7]:


def reverse_words(s):
    words = s.split()
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    result = " ".join(reversed_words)
    return result


# In[8]:


s = "Let's take LeetCode contest"
print(reverse_words(s))  # Output: "s'teL ekat edoCteeL tsetnoc"


# The output is "s'teL ekat edoCteeL tsetnoc" because each word in the sentence is reversed while preserving whitespace and the initial word order.

# # Q.5

# To reverse the first k characters for every 2k characters counting from the start of the string s, we can iterate over the string in chunks of size 2k and reverse the first k characters in each chunk.
# 
# Here's an algorithm to solve the problem:
# 
# Initialize an empty list result to store the final result.
# 
# Initialize a variable reverse_flag to True to indicate when to reverse the characters.
# 
# Iterate over the characters of s:
# If reverse_flag is True, reverse the first k characters in the current chunk and append them to result.
# 
# If reverse_flag is False, append the characters as they are to result.
# 
# Toggle the value of reverse_flag.
# 
# Join the characters in result into a single string and return it.

# In[9]:


def reverse_str(s, k):
    result = []
    reverse_flag = True

    for i in range(0, len(s), k):
        chunk = s[i:i+k]

        if reverse_flag:
            reversed_chunk = chunk[:k][::-1]
            result.append(reversed_chunk)
        else:
            result.append(chunk)

        reverse_flag = not reverse_flag

    return "".join(result)


# In[10]:


s = "abcdefg"
k = 2
print(reverse_str(s, k))  # Output: "bacdfeg"


# 

# # Q.6

# To determine if a string s can become goal after some number of shifts on s, we can check if goal is a substring of the concatenated string s + s.
# 
# Here's an algorithm to solve the problem:
# 
# Check if the lengths of s and goal are equal. If not, return False because they cannot be the same after any number of shifts.
# 
# Concatenate s with itself to form the string s_concat.
# 
# Check if goal is a substring of s_concat. If it is, return True; otherwise, return False.

# In[11]:


def can_shift(s, goal):
    if len(s) != len(goal):
        return False

    s_concat = s + s
    if goal in s_concat:
        return True
    else:
        return False


# In[12]:


s = "abcde"
goal = "cdeab"
print(can_shift(s, goal))  # Output: True


# The output is True because we can obtain goal by shifting s. In this case, abcde becomes bcdea after one shift, and then bcdea becomes cdeab after two more shifts.

# # Q. 7

# To determine if two strings s and t are equal when both are typed into empty text editors, considering that '#' represents a backspace character, we can simulate the typing process using stacks.
# 
# Here's an algorithm to solve the problem:
# 
# Define a helper function process_string(string) that takes a string as input and returns the final processed string after applying backspaces.
# 
# Initialize an empty stack stack.
# 
# Iterate over each character c in the string:
# If c is not a backspace character '#', push c onto the stack.
# 
# If c is a backspace character '#' and the stack is not empty, pop an element from the stack.
# 
# Convert the stack into a string and return it.
# 
# Call the process_string function on s and t, and compare the processed strings.
# 
# If the processed strings are equal, return True; otherwise, return False.

# In[13]:


def backspace_compare(s, t):
    def process_string(string):
        stack = []

        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()

        return ''.join(stack)

    return process_string(s) == process_string(t)


# In[14]:


s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))  # Output: True


# The output is True because both s and t become "ac" after applying the backspace characters.

# # Q.8

# To check if a given array of coordinates forms a straight line in the XY plane, we can calculate the slope between consecutive points and compare it with the slope between the first two points. If all slopes are equal, the points lie on the same straight line.
# 
# Here's an algorithm to solve the problem:
# 
# Check if the length of the coordinates array is less than 2. If it is, return True because a single point or no points are considered to be on a straight line.
# 
# Calculate the slope slope between the first two points (x1, y1) and (x2, y2) using the formula slope = (y2 - y1) / (x2 - x1).
# 
# Iterate over the remaining points in the coordinates array from index 2 onwards:
# Calculate the slope curr_slope between the current point (x, y) and the first point (x1, y1) using the formula curr_slope = (y - y1) / (x - x1).
# 
# If slope and curr_slope are not equal, return False because the points do not lie on the same straight line.
# 
# If the loop completes without returning False, return True because all points lie on the same straight line.

# In[15]:


def check_straight_line(coordinates):
    if len(coordinates) < 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        curr_slope = (y - y1) / (x - x1)
        if slope != curr_slope:
            return False

    return True


# In[16]:


coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(check_straight_line(coordinates))  # Output: True


# The output is True because all the given points form a straight line in the XY plane.

# In[ ]:




