# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:21:45 2020

@author: kingslayer
"""

#APRIORI

#importing the libraries
#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset=pd.read_csv("D:\work\ML A to Z\Machine Learning A-Z Template Folder\Part 5 - Association Rule Learning\Section 28 - Apriori\Market_Basket_Optimisation.csv",header=None)
transactions=[]
for i in range(7501):
    for j in range(20):
        transactions.append(str(dataset.values[i,j]))
    
#training Apriori
from apyori import apriori
rules=apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=2,min_length=2)

#Visualising results
results=list(rules)