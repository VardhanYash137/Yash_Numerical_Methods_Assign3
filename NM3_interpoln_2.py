#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Sample data
x = np.array([0,1,2,3,4,5])
y = np.array([1.0,2.0,1.0,0.5,4.0,8.0])

# Find the fifth-order Lagrange polynomial
poly = lagrange(x, y)

# Generate finer x values for smooth plotting
x_smooth = np.linspace(x.min(), x.max(), 1000)

# Evaluate the polynomial for the smooth x values
y_smooth = poly(x_smooth)

# Plotting the original data and Lagrange polynomial
plt.scatter(x, y, label='Data')
plt.plot(x_smooth, y_smooth, label='Lagrange Polynomial', linestyle='dashed')

plt.legend()
plt.title('Fifth-Order Lagrange Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# In[ ]:




