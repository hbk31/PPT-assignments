#!/usr/bin/env python
# coding: utf-8

# # Q.17

# In[1]:


def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


# In[2]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)


# # Q.18

#  Here's an implementation of the timer decorator function that measures the execution time of a function using the time module:

# In[3]:


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.5f} seconds")
        return result
    return wrapper


# In[10]:


@timer
def my_function():
    # Function code goes here
    time.sleep(3)

my_function()


# # Q19

# In[6]:


def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


# In[8]:


data = [15,45,85,50,35,20,5]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


# # Q.20

# In[11]:


from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value


# In[14]:


sample1 = [5, 10, 15, 20, 25,35, 40]
sample2 = [10, 20, 30, 40, 50 , 60, 70]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)


# In[ ]:




