from matplotlib import pyplot
from pandas import DataFrame
import numpy as np
import pandas as pd
import random
import copy
import random
import matplotlib.pyplot as plt
from scipy import stats


x_train = []
for i in range (100):
  x_train.append ( random.randint(1,100) )
x_train.sort()

m = random.randint(1,10)
c = random.randint(1,10)

print (m, c)

y_train = []
for i in range ( 100 ):
  y = m*x_train[i] + c + random.randint(1,50)
  y_train.append( y ) 


df = DataFrame(dict(X=x_train[:], Y=y_train[:]))
df.to_csv('Dataset.csv', index = False, header=True)

plt.scatter(x_train, y_train)
title = 'INPUT at m = ' + str(m) + ' and c = ' + str(c)
plt.title(title)

plt.show()