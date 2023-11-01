# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:07:07 2023
@author: Enrique Herrera

FLRW quantized solution
"""

from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np

#Parameters
Lmb = 10
c = 3
u = np.linspace(0,2,1000)

#Solution
psi = c*jv(0,4*(np.sqrt(Lmb/3))*np.exp(3*u))

#Squared solution
psi2 = psi**2
    
#Plot
plt.figure(0)
plt.plot(u,psi2,color="purple")
plt.grid()
plt.xlabel("u")
plt.ylabel(r'$\left|\Psi \right|^2$')
