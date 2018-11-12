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
data = pd.read_csv('C:/Users/user/Downloads/all_4_metrics_imdb.csv') 
fig, ax = plt.subplots(figsize=(7, 5))
 
x1 = list(data['TfIdf'])
x2 = list(data['L1NORM'])  
x3 = list(data['RBO'])
x4 = list(data['KL'])  

plt.xlim(0, 1)
 
 
sns.distplot(x1,label='TfIdf', hist = True, kde = False,norm_hist = True,
                 color=cc[0],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )
sns.distplot(x2,label='L1NORM',hist = True, kde = False,norm_hist = True,
                 color=cc[1],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )
sns.distplot(x3,label='RBO', hist = True, kde = False,norm_hist = True,
                 color=cc[2],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )
sns.distplot(x4, label='KL',hist = True, kde = False,norm_hist = True,
                 color=cc[3],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )

plt.xlabel('all words weights')

 
plt.ylabel('number of users')
plt.legend()

plt.show() 