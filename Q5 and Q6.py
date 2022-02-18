#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 04:56:58 2022

@author: jinhuili
"""
import pandas as pd 
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.linalg as la
df = pd.read_excel("Q5.xlsx")
w1 = df.iloc[0]
w2 = df.iloc[1]
w3 = df.iloc[2]
w4 = df.iloc[3]
w5 = df.iloc[4]
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
for i in range(9):
    value = math.log(w1[i+1]/w1[i])
    x1.append(value)
for i in range(9):
    value = math.log(w2[i+1]/w2[i])
    x2.append(value)
for i in range(9):
    value = math.log(w3[i+1]/w3[i])
    x3.append(value)
for i in range(9):
    value = math.log(w4[i+1]/w4[i])
    x4.append(value)
for i in range(9):
    value = math.log(w5[i+1]/w5[i])
    x5.append(value)
X=[x1,x2,x3,x4,x5]
Firstcovariance=np.cov(X)
print(Firstcovariance)
print(np.linalg.eig(Firstcovariance))
forward = [0.027296984634014088, 0.031754304563520463, 0.033993849964036205, 0.03485132409162306, 0.026284807236626406, 0.030935846857997884, 0.03323033723937252, 0.03424734030988619, 0.027709456615739647, 0.03186273596914724, 0.03378756576284481, 0.0348035716147872, 0.028120257573122753, 0.03196888784055529, 0.03357817997266066, 0.03453734467767022, 0.02853319136147725, 0.032804695048961996, 0.03415143101300444, 0.035136173813124394, 0.03039237421651997, 0.0344898359090724, 0.03566887718511991, 0.036647259662238696, 0.03081547017869868, 0.03523554144483043, 0.036828676264104576, 0.03772413249813722, 0.03040982829452954, 0.03513659585985174, 0.036906948182322985, 0.03783950395359437, 0.03162922559462045, 0.03574920610843302, 0.03710342971749592, 0.03795821026304358, 0.03120802862216454, 0.03458885025610536, 0.036160178886561756, 0.03683017186617343]
q1 =[forward [x] for x in [0,4,8,12,16,20,24,28,32,36]]
q2 = [forward [x] for x in [1,5,9,13,17,21,25,29,33,37]]
q3 = [forward [x] for x in [2,6,10,14,18,22,26,30,34,38]]
q4 = [forward [x] for x in [3,7,11,15,19,23,27,31,35,39]]
o1=[]
o2=[]
o3=[]
o4=[]
for i in range(9):
    value = math.log(q1[i+1]/q1[i])
    o1.append(value)
for i in range(9):
    value = math.log(q2[i+1]/q2[i])
    o2.append(value)
for i in range(9):
    value = math.log(q3[i+1]/q3[i])
    o3.append(value)
for i in range(9):
    value = math.log(q4[i+1]/q4[i])
    o4.append(value)
Secondcovariance = np.cov([o1,o2,o3,o4])  
print(Secondcovariance)
print(np.linalg.eig(Secondcovariance))