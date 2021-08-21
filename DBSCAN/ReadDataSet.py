# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:32:41 2021

@author: Mueed
"""
from sklearn.datasets import make_moons
from matplotlib import pyplot
from pandas import DataFrame
import pandas as pd
import random



X, y = make_moons(n_samples=200, shuffle=True, noise=None, random_state=None)
df = DataFrame(dict(x1=X[:,0]+1, x2=X[:,1]+0.5, label=0))
df=df.append({'x1':0.5,'x2':0.2,'label':0},ignore_index=True)
df=df.append({'x1':0.3,'x2':0.9,'label':0},ignore_index=True)
df=df.append({'x1':2.5,'x2':1.2,'label':0},ignore_index=True)
df=df.append({'x1':1.5,'x2':1,'label':0},ignore_index=True)
df=df.append({'x1':3,'x2':0.2,'label':0},ignore_index=True)
#df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('moonDataset.csv', index = False, header=True)





grouped = df.groupby('label')

fig, ax = pyplot.subplots()
for key, group in grouped:
    labels = "Cluster: "+ str(int(key))
    rgb = (random.random(), random.random(), random.random())
    group.plot(title="Input Data", ax=ax, kind='scatter', x='x1', y='x2', label=labels, color=rgb)
pyplot.show()
