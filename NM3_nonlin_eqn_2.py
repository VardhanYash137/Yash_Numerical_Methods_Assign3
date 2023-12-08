#!/usr/bin/env python
# coding: utf-8

# In[4]:


from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def function(x):
    return np.sin(np.cos(np.exp(x)))

def plot_function(f):
    x_ran=np.linspace(-10,10,1000)
    plt.plot(x_ran,f(x_ran),".-b")
    plt.grid()
    plt.show()

def derivative(x):
    return -np.exp(x) * np.cos(np.cos(np.exp(x))) * np.sin(np.exp(x))

# Initial guess -1
root_1 = newton(function, -1, fprime=derivative)

# Initial guess -0.1
root_2 = newton(function, -0.1, fprime=derivative)

#not specifying the derivative
root_3 = newton(function,-0.1)

# Print the results
print("Root with initial guess -1:", root_1)
print("Root with initial guess -0.1:", root_2)
print("Root with initial guess -0.1 (with secant) :", root_3)
plot_function(function)


# In[5]:


help(newton)


# In[ ]:




