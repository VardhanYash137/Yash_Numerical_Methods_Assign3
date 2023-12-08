#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.optimize import bisect
import numpy as np

# Define the function
def equation(x):
    return np.sin(np.cos(np.exp(x)))

# Initial bracket
a = -1
b = 1

# Find the root using the bisection method
root = bisect(equation, a, b)

# Calculate the function value at the root
value_at_root = equation(root)

# Print the result
print("Root:", root)
print("Value of sin(cos(exp(x))) at the root:", value_at_root)


# In[4]:


help(bisect)


# In[ ]:




