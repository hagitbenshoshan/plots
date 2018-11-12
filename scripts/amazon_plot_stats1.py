# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:09:08 2018

@author: user

Vocabulary_size

"""

 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="white", context="talk")
cc = sns.color_palette('Set1')
data = pd.read_csv('C:/Users/user/Downloads/amazon.csv') 
fig, ax = plt.subplots(figsize=(7, 5))
 
x2 = list(data['Vocabulary Size'])

plt.ylim(1, 10000) 
plt.xlim(0, 12000) 
 

sns.distplot(x2,hist = True, kde = False,   color="darkcyan",
                  bins=250 , kde_kws = {'linewidth': 1 },
                  hist_kws={ 'edgecolor':'black', "rwidth":1,  'alpha':0.5  }) 
 
plt.xlabel('Vocabulary Size')
plt.ylabel('number of users')

plt.show() 