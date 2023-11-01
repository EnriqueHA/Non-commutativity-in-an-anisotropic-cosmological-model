# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:30:01 2022

@author: Enrique Herrera
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#Parameters
eta = 0.05
kappa = 0.5
lmda = 10
a = 0.5
b = 5#25
c = 2*np.sqrt(2*lmda/3)*(1/np.pi) #Constants which multiplicates the integrand
th1 = 0#0.1
th2 = 0#0.15
th3 = 0#0.2

#Default values
u = np.linspace(0,4,45) #(0,4,40)
v = np.linspace(-40,40,45)
U,V = np.meshgrid(u,v)
results = [0]*len(u)

#Numerical solution
for x in u:
    result_row = []
    argJn = c*np.exp(3*(x-0.5*th1*eta+0.5*th3*kappa))
    f = lambda t,n: np.exp(-a*(0.25*np.sqrt(16*n**2+1)-b)**2)*np.cos(0.25*np.sqrt(16*n**2+1)*t-argJn*np.sin(t))
    tuple_result = integrate.dblquad(f,-np.inf,np.inf,0,np.pi)
    result = tuple_result[0]
    
    for y in v:
       result = np.exp(-eta*y)*result/(2*np.sqrt(3*lmda)*np.exp(3*x))**(1/4)
        
       #Multiplicates by conjugate to obtain |Psi|^2 as final result
       result_row.append(result*np.conj(result))
        
    result_row = np.array(result_row)
    #Create an array through we will be able to plot
    results = np.vstack((results,result_row))

results = np.delete(results,0,0)

#Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_xlabel('u')
ax.set_ylabel('v')
surf = ax.plot_surface(U,V,results,cmap='viridis')
plt.show()