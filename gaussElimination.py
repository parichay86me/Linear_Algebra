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

# LU Decomposition: DoLittle's Decomposition| Ax=b -> LUx=b

import numpy as np

def lu_Decomp(a,B):
    
    A=np.array(a,float)
    b=np.array(B,float)
    n=len(b)
    y=np.zeros([n,1])
    x=np.zeros([n,1])
    
    for k in range(0,n-1):
        
        for i in range(k+1,n):
            
            if A[i,k]!=0:
                lam=A[i,k]/A[k,k]
                
                for j in range(k+1,n):
                    A[i,j]=A[i,j]-(lam*A[k,j])
                
                A[i,k]=lam
                
            else:
                pass
            
    y[0]=b[0]        
    for k in range(1,n):
        y[k]=b[k]-np.dot(A[k,0:k],y[0:k])
        
    for k in range(n-1,-1,-1):
        x[k]=(y[k]-np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]
        
    print(A)
    print(y)
    return x
       
lu_Decomp([[2,1,0],[1,2,1],[0,1,2]],[4,8,8])

# Choleski's Decomposition: Ax=b -> LL'x=b   

import numpy as np

def check_choleski(a):
    
    A=np.array(a,float)
    n=len(A)
    L=np.zeros([n,n])
    
    
               
check_choleski([[2,1,0],[1,2,1],[0,1,2]])
check_choleski([[1,0,1],[1,1,0],[0,1,1]])     
    
    
               
             
              
                                
                
             
                
                            
         
              
        
    
                
