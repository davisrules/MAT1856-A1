#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:59:19 2022

@author: jinhuili
"""
from sympy import symbols, solve
import pandas as pd 
import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel("book2.xlsx")
x = np.linspace(0.5,5,num=10,endpoint = True)
y1 = df["Jan.10"]
y2 = df["Jan.11"]
y3 = df["Jan.12"]
y4 = df["Jan.13"]
y5 = df["Jan.14"]
y6 = df["Jan.17"]
y7 = df["Jan.18"]
y8 = df["Jan.19"]
y9 = df["Jan.20"]
y10 = df["Jan.21"]
plt.plot(x,y1,'-',x,y2,'-',x,y3,'-',x,y4,'-',x,y5,'-',x,y6,'-',x,y7,'-',x,y8,'-',x,y9,'-',x,y10,'-')
plt.xlabel("years to maturity")
plt.ylabel("Bonds yield(ytm)")
plt.title('5-year yield curve(ytm curve)')
plt.legend(["Jan.10.2022","Jan.11.2022","Jan.12.2022","Jan.13.2022","Jan.14.2022","Jan.17.2022","Jan.18.2022","Jan.19.2022","Jan.20.2022","Jan.21.2022"],loc='center left',bbox_to_anchor=(1, 0.5))
