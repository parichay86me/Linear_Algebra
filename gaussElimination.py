# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:11:03 2022

@author: parichay.basu
"""
# Gauss Elimination: Ax=b -> Ux=c

import numpy as np

def gaussElimin(a,B):
    
    A=np.array(a,float)
    b=np.array(B,float)
    n=len(b)
    x=np.zeros([n,1])
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k]!=0:
                lam=A[i,k]/A[k,k]
                A[i,k:n]=A[i,k:n]-lam*A[k,k:n]
                b[i]=b[i]-lam*b[k]
    
    for k in range(n-1,-1,-1):
        x[k]=(b[k]-np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
    return x
    #print(A)
    
gaussElimin([[1,3],[2,5]],[7,12])


    
    
               
             
              
                                
                
             
                
                            
         
              
        
    
                
