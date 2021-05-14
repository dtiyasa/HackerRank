# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:36:15 2021

@author: tiyasa dey
"""

T=int(input())
ns=[]
arr1=[]

for i in range(T):
    n=input().split(" ")
    ns.append(n)
    arr1.append(input().split(" "))
    
for i in range(T):
    n=ns[i]
    arr=arr1[i]
    for i in range(len(arr)):
        arr[i]=int(arr[i])
        
    arr.reverse()
    print(arr)