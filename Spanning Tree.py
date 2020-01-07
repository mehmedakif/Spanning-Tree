# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:07:03 2019

@author: Akif
"""

import numpy as np

adjency = np.array([
       [0,1,1,0,1,0,1,0],
       [1,0,1,1,0,1,0,1],
       [1,1,0,1,0,0,1,0],
       [0,1,1,0,1,101,1],
       [1,0,0,1,0,0,1,0],
       [0,1,0,1,0,0,1,0],
       [1,0,1,0,1,1,0,1],
       [0,1,0,1,0,0,1,0],
       ])

laplacian = np.zeros((8,8))


for i in range(len(adjency)):
    for j in range(len(adjency[i])):
        if adjency[i][j]==1:
            laplacian[i][i] = laplacian[i][i]+1
            laplacian[i][j]=-1
     
laplacian = np.delete(laplacian,0,0)        
laplacian = np.delete(laplacian,0,1) 

print(np.linalg.det(laplacian))

