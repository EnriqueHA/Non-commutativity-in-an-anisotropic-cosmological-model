# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 01:31:22 2023

@author: dq131
"""

import numpy as np
import matplotlib.pyplot as plt

#Parameters
Lmbda = 1
c2 = np.sqrt(3*Lmbda)
c1 = 3

#Solution
def u_sol(c1, c2, sign):
    if sign == 'negative':
        t = np.linspace(-20,-c1-0.3,1000)
        return t, (1/3)*np.log(-1/(c2*t+c2*c1))
    
    elif sign == 'positive':
        t = np.linspace(-c1+.3,20,1000)
        return t, (1/3)*np.log(1/(c2*t+c2*c1))

u1 = u_sol(c1, c2, 'negative')
u2 = u_sol(c1, c2, 'positive')
u3 = u_sol(-c1, c2, 'negative')
u4 = u_sol(-c1, c2, 'positive')


#Plot
plt.figure(0)
plt.plot(u1[0],u1[1],color="purple", label=r"$C>0$")
plt.plot(u2[0],u2[1],color="purple")
plt.plot(u3[0],u3[1],color="green", label=r"$C<0$")
plt.plot(u4[0],u4[1],color="green")
plt.legend()
plt.grid()
plt.xlabel("t")
plt.ylabel('u(t)')