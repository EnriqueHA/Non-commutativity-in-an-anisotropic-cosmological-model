# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:05:43 2022
Copied on Sep 24 2023
@author: Enrique Herrera
"""

import numpy as np
import matplotlib.pyplot as plt

#Parameters
p0v = 0.4
p0w = 0.4
A = np.sqrt(p0v**2 + p0w**2)
lmbda = 1
C = 3

#Time
t1 = np.linspace(-20,20,1000)
t2 = np.linspace(-20,-C,1000)
t3 = np.linspace(-20,-C-0.04,1000)
t4 = np.linspace(-C+0.04, 20, 1000)

#Functions
u1 = -(1/12)*A*t1
u2 = (1/6)*np.log(A**2/(48*lmbda*(np.cosh(A*(t2+C)/4))**2))
u3 = (1/6)*np.log(A**2/(48*lmbda*(np.sinh(A*(t3+C)/4))**2))
u4 = (1/6)*np.log(A**2/(48*lmbda*(np.sinh(A*(t4+C)/4))**2))
v = (1/12)*p0v*t1
w = (1/12)*p0w*t1

#Plot
plt.figure(1)
plt.xlabel('t')
plt.plot(t1,u1, color='orange', label = r'$u(t)$, $\Lambda = 0$, $\dot{u} <0$')
plt.plot(t2,u2, color='blue', label = r'$u(t)$, $\Lambda < 0$')
plt.plot(t3,u3, color='red', label = r'$u(t)$, $\Lambda > 0$')
plt.plot(t1,v, color='green', label = r'$v(t)$')
plt.axvline(x = -C, color = 'grey', linestyle = 'dashed', label = '-C')
plt.plot(t4,u4, color='red')
plt.grid()
plt.legend()
plt.show()