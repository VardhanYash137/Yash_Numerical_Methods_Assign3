#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
import pandas as pd

def error_interpolating_poly(x_values,fname,f):
    y_values = f(x_values)

    # Lagrange interpolation polynomial
    poly = lagrange(x_values, y_values)
    
    # Fit a linear spline
    linear_spline = InterpolatedUnivariateSpline(x_values, y_values, k=1)

    # Fit a quadratic spline
    quadratic_spline = InterpolatedUnivariateSpline(x_values, y_values, k=2)
    
    # Interpolate at x = 0.45
    x_interpolate = 0.45
    y_interpolated = poly(x_interpolate)
    y_interpolated1 = linear_spline(x_interpolate)
    y_interpolated2 = quadratic_spline(x_interpolate)
    
    #Continuous value of x array
    x_smooth=np.linspace(x_values.min(),x_values.max(),100)

    # True value at x = 0.45
    true_value = np.cos(x_interpolate)

    # Absolute error
    absolute_error = np.abs(true_value - y_interpolated)
    absolute_error1 = np.abs(true_value - y_interpolated1)
    absolute_error2 = np.abs(true_value - y_interpolated2)
    
    
    plt.scatter(x_values,y_values,label="Given data points")
    plt.plot(x_smooth,linear_spline(x_smooth),label="Linear Spline Interpolated Function",linestyle='dashed')
    plt.plot(x_smooth,quadratic_spline(x_smooth),label="Quadratic Spline Interpolated Function",linestyle='dashed')
    plt.plot(x_smooth,poly(x_smooth),label="Lagrange Interpolated Function",linestyle='dashed')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fname)
    plt.legend()
    plt.grid()
    plt.show()
    
    method_list=["lagrange","linear spline","quadratic spline"]
    abs_err_list=[absolute_error,absolute_error1,absolute_error2]
    int_value_list=[y_interpolated,y_interpolated1,y_interpolated2]
    
    data_mat=np.column_stack((method_list,int_value_list,abs_err_list))
    df1=pd.DataFrame(data_mat,columns=("methods","Interpolated value at x=0.45","absolute error"))
    
    print("True value at x = 0.45:", true_value)
    print(df1)
    

    

x_values=np.array([0, 0.6, 0.9])
error_interpolating_poly(x_values,"Cos fn",np.cos)
error_interpolating_poly(x_values,"sqrt(1+x)",f=lambda x: np.sqrt(1+x))
error_interpolating_poly(x_values,"log(1+x)",f=lambda x: np.log(1+x))
error_interpolating_poly(x_values,"tan fn",np.tan)



# In[ ]:




