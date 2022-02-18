#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:09:42 2022

@author: jinhuili
"""
import pandas as pd 
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.linalg as la
df = pd.read_excel("excel for Assignment 1.xlsx")
P0 = df["Jan.10"]
P1 = df["Jan.11"]
P2 = df["Jan.12"]
P3 = df["Jan.13"]
P4 = df["Jan.14"]
P5 = df["Jan.17"]
P6 = df["Jan.18"]
P7 = df["Jan.19"]
P8 = df["Jan.20"]
P9 = df["Jan.21"]
coupon = df["Maturity"]
A = [P0,P1,P2,P3,P4,P5,P6,P7,P8,P9]
spot =[]
t = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
for k in A:
    for i in range(10):
        sum = 0
        value =0
        for j in range(0,i):
            if  i==0:
                sum =0 
            else:
                sum += coupon[i]/2*100*math.exp(-spot[j]*t[j])
        value = (math.log((k[i]-sum)/(100+coupon[i]/2*100)))/-t[i]
        spot.append(value)    
y1 = spot[:10]
y2 = spot[10:20]
y3 = spot[20:30]
y4 = spot[30:40]
y5 = spot[40:50]
y6 = spot[50:60]
y7 = spot[60:70]
y8 = spot[70:80]
y9 = spot[80:90]
y10 = spot[90:100]
x = np.linspace(0.5,5,num=10,endpoint = True)

plt.plot(x,y1,'-',x,y2,'-',x,y3,'-',x,y4,'-',x,y5,'-',x,y6,'-',x,y7,'-',x,y8,'-',x,y9,'-',x,y10,'-')
plt.xlabel("Time to Maturity(Units years) ")
plt.ylabel("Spot Rate")
plt.title("Spot Curve fomr Jan.10 to Jan.21")
plt.legend(["Jan.10.2022","Jan.11.2022","Jan.12.2022","Jan.13.2022","Jan.14.2022","Jan.17.2022","Jan.18.2022","Jan.19.2022","Jan.20.2022","Jan.21.2022"],loc='center left',bbox_to_anchor=(1, 0.5))
