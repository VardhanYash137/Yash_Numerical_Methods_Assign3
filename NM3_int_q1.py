#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.integrate import trapezoid, simpson, romberg

# Define the function to be integrated
def f(x):
    return np.exp(x)

# Define the integration limits
a = 0
b = 1

# Number of points for integration
num_points = 2  # You can adjust this based on your requirement

# Generate the x values
x_values = np.linspace(a, b, num_points)

# Compute the integral using the Trapezoidal rule
trapezoidal_result = trapezoid(f(x_values), x=x_values)

# Compute the integral using Simpson's rule
simpson_result = simpson(f(x_values), x=x_values)

# Compute the integral using Romberg method
romberg_result = romberg(f, a, b)

# Print the results
print("Trapezoidal Rule Result:", trapezoidal_result)
print("Simpson's Rule Result:", simpson_result)
print("Romberg Method Result:", romberg_result)


# In[ ]:




