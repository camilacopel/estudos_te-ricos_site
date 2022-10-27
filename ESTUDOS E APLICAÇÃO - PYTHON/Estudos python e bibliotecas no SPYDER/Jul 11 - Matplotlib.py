# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:57:50 2022

@author: E805511
"""

#UTILIZAÇÃO DA BIBLIOTECA PANDAS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.Series([.25, .5, .75, 1.],
                 index=["a", "b", 'c', 'd'] or [1,2,3,4],
                 )
print(data)

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 20))
print(ser)

#%% FAZENDO TABELAS 
#Atividades Operations 
"------------"

#%% CUSTOMIZING MATPLOTLIB
import array


#%% CUSTOMIZING MATPLOTLIB 2
x = [np.arange(0, 10, 2)]
x1 = [np.arange(1, 10, 2)]
y = array[1, 3, 3, 7, 8]

plt.plot(x, '-', marker  = 'd'), (y, '--')
plt.plot(x1, '-', marker  = 'd'), (y, '-')
plt.show()
