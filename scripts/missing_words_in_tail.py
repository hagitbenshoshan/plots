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
data = pd.read_csv('C:/Users/user/Downloads/imdb_missing_in_tail.csv') 
fig, ax = plt.subplots(figsize=(7, 5))
 
x2 = list(data['missing_words_weight'])  
x3 = list(data['L1missing_words_weight']) 

#   missing words in head 

 
sns.distplot(x3, label='L1-Norm missing words',hist = True, kde = False,norm_hist = True,
                 color=cc[1],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )

sns.distplot(x2, label='KL missing words',hist = True, kde = False,norm_hist = True,
                 color=cc[3],
                 bins=20, kde_kws = {'linewidth': 1 },
                 hist_kws={ 'edgecolor':'black', "rwidth":1 , 'alpha':0.65  } )
 
plt.ylim(0, 12) 
plt.xlim(0, 0.5) 
plt.legend(loc='upper center') 
plt.xlabel('missing words weights') 
plt.ylabel('number of users')
plt.legend()

plt.show() 