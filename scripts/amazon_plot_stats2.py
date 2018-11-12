# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:09:08 2018

@author: user

Missing words % in top 1000

"""

# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style="white", context="talk")
cc = sns.color_palette('Set1')
data = pd.read_csv('C:/Users/user/Downloads/amazon.csv') 
fig, ax = plt.subplots(figsize=(7, 5))
 
x2 = list(data['missing words %'])

plt.ylim(1, 400) 
plt.xlim(0, 100) 
 

sns.distplot(x2,hist = True, kde = False,   color="darkcyan",
                  bins=250 , kde_kws = {'linewidth': 1 },
                  hist_kws={ 'edgecolor':'black', "rwidth":1,  'alpha':0.5  }) 
 
plt.xlabel('Missing words % in top 1000')
plt.ylabel('number of users')

plt.show()
  