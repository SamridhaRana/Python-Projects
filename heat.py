# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 13:20:10 2021

@author: Samridha
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

deltaT = 0.004
deltaX = 0.1


Lt = 1

N = int(1/deltaX)
A = int(1/deltaT)


sigma = deltaT/(deltaX**2)
#The function stiffmatrix creates the stiff matrix.
M = np.zeros((N-1,N-1))

def stiffmatrix(M):
    for i in range(0,N-1):
        M[i][i] = 1 - 2 * sigma
        if i+1 != N-1:
            M[i+1][i] = sigma
        if i+1 != N-1:
            M[i][i+1] = sigma
        M[N-2][N-2] = 1 - 2 * sigma
    print(M)
        
stiffmatrix(M)

#Now to find the solution matrix

initial_value = np.ones((N+1,1))
for i in range(N+1):
    initial_value[i,0] = np.sin(2 * np.pi * deltaX*i)** 2
    
initial_u = np.ones((N-1,1))

for i in range(N-1):
    initial_u[i,0] = initial_value[i+1,0]   
    

value = [initial_value]

temp = np.zeros((N-1,1))
temp = M.dot(initial_u)
array = np.zeros((N+1,1))

for i in range(N-1):
    array[i+1,0] = temp[i,0]
value.append(array)

for i in range(1,A):
    temp = M.dot(temp)
    array = np.zeros((N+1,1))
    
    for i in range(N-1):
        array[i+1, 0] = temp[i,0]
        
    value.append(array)
    
final_u = np.zeros((A+1,N+1))

t = 0
for i in range(A+1):
    for j in range(N+1):
        final_u[i,j] = value[i][j,0]
        t = t + 1
            
plt.imshow(final_u, cmap='plasma', aspect='auto' , origin='lower')
plt.show()        
     
#this function is used to make graphs a 3d plot
def grapher(x,t):
    fig = plt.figure()
    ax = Axes3D(fig)
    X, T = np.meshgrid(x, t)
    ax.plot_surface(X, T, final_u, rstride=1, cstride=1,)
    plt.plot(t,x)
    
x = np.arange(0,1.00001,deltaX)
t = np.arange(0,1.00001,deltaT)
grapher(x,t)

#for part 2 with boundary conditions set at 20 and 50 you need to uncomment this part so you can 
#process the part 2 of the lab 

# boundStart = 20
# boundEnd = 50
# bound = np.zeros((N-1,1))
# bound[0,0]=boundStart
# bound[-1,0] = boundEnd
# initial_u = np.ones((N-1,1))
# for i in range(N-1):
#     initialU[i,0] = 0
# values = [initial_u]

# temp = M.dot(initial_u)
# temp = temp + bound
# values.append(temp)

# for i in range(1,A):
#     temp = M.dot(temp)
#     temp = temp + bound
    
#     values.append(temp)

# final_u = np.zeros((A+1,N+1))

# for i in range(A+1):
#     final_u[i,0] = boundStart
#     final_u[i,N] = boundEnd
    
# k = 0
# for i in range(A+1):
#     for j in range(N+1):
#         if j!=0 and j!= N:
#             final_u[i,j] = values[i][j-1]
#             k = k +  1

   
# plt.imshow(final_u, cmap='plasma', aspect='auto' , origin='lower')
# plt.show()       

# def grapher(x,t):
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     X, T = np.meshgrid(x, t)
#     ax.plot_surface(X, T, final_u, rstride=1, cstride=1,)
#     plt.plot(t,x)
     
# x = np.arange(0,1.000001,deltaX)
# t = np.arange(0,1.000001,deltaT)

# grapher(x,t)




