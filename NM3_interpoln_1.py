#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline


# Sample data
x = np.array([0,1,2,3,4,5])
y = np.array([1.0,2.0,1.0,0.5,4.0,8.0])

# Fit a linear spline
linear_spline = InterpolatedUnivariateSpline(x, y, k=1)

# Fit a quadratic spline
quadratic_spline = InterpolatedUnivariateSpline(x, y, k=2)

# Fit a cubic spline
cubic_spline = InterpolatedUnivariateSpline(x, y, k=3)

# Generate finer x values for smooth plotting
x_smooth = np.linspace(x.min(), x.max(), 1000)

# Plotting the original data and fitted splines
plt.scatter(x, y, label='Data')
plt.plot(x_smooth, linear_spline(x_smooth), label='Linear Spline', linestyle='dashed')
plt.plot(x_smooth, quadratic_spline(x_smooth), label='Quadratic Spline', linestyle='dashed')
plt.plot(x_smooth, cubic_spline(x_smooth), label='Cubic Spline', linestyle='dashed')

plt.legend()
plt.title('Fitting Splines to Data')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




