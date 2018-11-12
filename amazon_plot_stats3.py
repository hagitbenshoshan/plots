# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:56:42 2018

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:09:08 2018

@author: user
"""

# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
 
data = pd.read_csv('C:/Users/user/Downloads/amazon.csv') 
cc = sns.color_palette('Set1')
fig, ax = plt.subplots(figsize=(7, 5))

g = sns.regplot(x="Vocabulary Size", y="missing words %", data=data , ci = False,
    scatter_kws={"color":cc[1],"alpha":0.3,"s":20},
    line_kws={"color":"b","alpha":0.0,"lw":4,'label':'Joint Clustering'},marker="x")
#upper/lower limits of axis
plt.ylim(0, 100) 
plt.xlim(0, 15000) 
plt.ylabel('missing words %')
plt.xlabel('Vocabulary Size')
plt.show() 