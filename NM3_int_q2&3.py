#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from scipy.integrate import trapezoid, simpson, romberg

def integration_trap_composite(f,n,a,b):
    x_values = np.linspace(a,b,n+1)
    trapezoidal_result = trapezoid(f(x_values), x=x_values)
    return trapezoidal_result

def integration_simp_composite(f,n,a,b):
    x_values = np.linspace(a,b,n+1)
    trapezoidal_result = simpson(f(x_values), x=x_values)
    return trapezoidal_result

def f1(x):
    return x * np.log(x)

def f2(x):
    return 2 / (x**2 + 4)

def f3(x):
    return np.tan(x)

print("Trapezoidal Composite Rule")
print("Integration of xln(x) between a=1 and b=2: ",integration_trap_composite(f1,4,1,2))
print("Integration of 2/(x^2+4) between a=0 and b=2: ",integration_trap_composite(f2,6,0,2))
print("Integration of tan(x) between 0 and 3pi/8: ",integration_trap_composite(f3,8,0,3*np.pi/8))

print()
print("Simpson Composite Rule")
print("Integration of xln(x) between a=1 and b=2: ",integration_simp_composite(f1,4,1,2))
print("Integration of 2/(x^2+4) between a=0 and b=2: ",integration_simp_composite(f2,6,0,2))
print("Integration of tan(x) between 0 and 3pi/8: ",integration_simp_composite(f3,8,0,3*np.pi/8))



# In[ ]:




