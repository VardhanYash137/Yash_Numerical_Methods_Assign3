#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from scipy.integrate import romberg

# Function to be integrated
def f1(x):
    return x**2 * np.log(x)

def f2(x):
    return x**2 * np.exp(-x)

def f3(x):
    return (np.cos(x))**2

# Interval
a1, b1 = 1, 1.5
a2, b2 = 0,1
a3, b3 = 0, ((np.pi)/4)

# Romberg integration
result1 = romberg(f1, a1, b1)
result2 = romberg(f2, a2, b2)
result3 = romberg(f3, a3, b3)

print("Result for integral 1:", result1)
print("Result for integral 2:", result2)
print("Result for integral 3:", result3)


# In[ ]:




