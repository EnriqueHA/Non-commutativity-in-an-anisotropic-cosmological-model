# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:05:43 2022
Copied on Sep 24 2023
@author: Enrique Herrera
"""

import numpy as np
import matplotlib.pyplot as plt

#Parameters
p0v = -0.4
p0w = -0.4
A = np.sqrt(p0v**2 + p0w**2)
lmbda = 1
C = -3
th1 = 0.1
th3 = 0.5

#Time
t1 = np.linspace(-20,-C-0.3,1000)
t2 = np.linspace(-C+0.3,20,1000)
t3 = np.linspace(-20,-C-.06,1000)
t4 = np.linspace(-C+.06,20,1000)

#Functions
#(It depends on what solution we are looking for) 

#u0 = -(1/12)*A*t1
#u1 = (1/6)*np.log(A**2/(48*lmbda*(np.cosh(A*(t1+C)/4))**2)) + 0.5*th1*p0v - 0.5*th3*p0w
u2 = (1/6)*np.log(A**2/(48*lmbda*(np.sinh(A*(t3+C)/4))**2)) + 0.5*th1*p0v - 0.5*th3*p0w
#v0 = (1/12)*p0v*t1
#v1 = (1/12)*p0v*t1 - 0.5*th1*A*np.tanh(A*(t1+C)) 
v2 = (1/12)*p0v*t3 + 0.5*th1*A*(1/np.tanh(A*(t3+C)))
#w0 = (1/12)*p0w*t1
#w1 = (1/12)*p0v*t1 + 0.5*th3*A*np.tanh(A*(t1+C))
w2 = (1/12)*p0v*t1 - 0.5*th3*A*(1/np.tanh(A*(t1+C)))

#This is to represent better both parts of the solution, separating it
u22 = (1/6)*np.log(A**2/(48*lmbda*(np.sinh(A*(t4+C)/4))**2)) + 0.5*th1*p0v - 0.5*th3*p0w
v22 = (1/12)*p0v*t4 + 0.5*th1*A*(1/np.tanh(A*(t4+C)))
w22 = (1/12)*p0v*t2 - 0.5*th3*A*(1/np.tanh(A*(t2+C)))

#Plot
plt.figure(1)
plt.title(r'$\Lambda>0$')
plt.xlabel('t')
plt.plot(t1,u2,color='red', label = r'$u(t)$')
plt.plot(t1,v2,color='green', label = r'$v(t)$')
plt.plot(t1,w2,color='blue', label = r'$w(t)$')
plt.plot(t2,u22,color='red')
plt.plot(t2,v22,color='green')
plt.plot(t2,w22,color='blue')
plt.axvline(x = -C, color = 'grey', linestyle = 'dashed', label = '-C')
plt.grid()
plt.legend()
plt.show()