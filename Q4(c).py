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


F1 = [spot [x] for x in [3,5,7,9]]
F2 = [spot [x] for x in [13,15,17,19]]
F3 = [spot [x] for x in [23,25,27,29]]
F4 = [spot [x] for x in [33,35,37,39]]
F5 = [spot [x] for x in [43,45,47,49]]
F6 = [spot [x] for x in [53,55,57,59]]
F7 = [spot [x] for x in [63,65,67,69]]
F8 = [spot [x] for x in [73,75,77,79]]
F9 = [spot [x] for x in [83,85,87,89]]
F10 = [spot [x] for x in [93,95,97,99]]
B = [F1,F2,F3,F4,F5,F6,F7,F8,F9,F10]
Start = [spot[x] for x in [1,11,21,31,41,51,61,71,81,91]]
forward = []
for i in range(10):   
    for j in range(2,6):
        rate = (((1+B[i][j-2])**(2*j)/((1+Start[i])**2))**(1/(2*j-2))-1)*2
        forward.append(rate)

w1 = forward[:4]
w2 = forward[4:8]
w3 = forward[8:12]
w4 = forward[12:16]
w5 = forward [16:20]
w6 = forward [20:24]
w7 = forward [24:28]
w8 = forward [28:32]
w9 = forward [32:36]
w10 = forward [36:40]
xnew = ["1yr-2yr","1yr-3yr","1yr-4yr","1yr-5yr"]
plt.plot(xnew,w1,'-',xnew,w2,'-',xnew,w3,'-',xnew,w4,'-',xnew,w5,'-',xnew,w6,'-',xnew,w7,'-',xnew,w8,'-',xnew,w1,'-',xnew,w9,'-',xnew,w10,'-')
plt.xlabel("time periods")
plt.ylabel("forward rate")
plt.title("1-year forward curve")
plt.legend(["Jan.10.2022","Jan.11.2022","Jan.12.2022","Jan.13.2022","Jan.14.2022","Jan.17.2022","Jan.18.2022","Jan.19.2022","Jan.20.2022","Jan.21.2022"],loc='center left',bbox_to_anchor=(1, 0.5))

        
    

    
