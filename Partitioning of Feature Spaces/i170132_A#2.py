#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


# In[2]:


iris_allCols=pd.read_csv('iris.csv',header=None)
iris=iris_allCols[[0,1,4]]
iris.to_csv('train.csv',header=['sepal_length','sepal_width','class_label'])
df=pd.read_csv('train.csv')
grouped = df.groupby('class_label')
colors = ["red", "blue","green"]
fig, ax = plt.subplots()
i=0
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='sepal_length', y='sepal_width', label=key, color=colors[i])
    i+=1
plt.show()


# In[3]:


def entropy(data,n):
  entropy=[]
  total=len(data)
  split_length=0
  min_ent=1000
  labels=np.unique(data[:,2])
  lengths=np.unique(data[:,n])
  for x in lengths:
    less=np.count_nonzero(data[:,n]<=x)
    greater=np.count_nonzero(data[:,n]>x)
    data1=data[data[:,n]<=x]
    data2=data[data[:,n]>x]
    E1=0
    E2=0
    for label in labels:
      Y1=np.count_nonzero(data1[:,2]== label )
      P1=Y1/less
      if(P1!=0):
        E1-=P1*np.log2(P1)
      Y2=np.count_nonzero(data2[:,2]== label )
      if(greater!=0):
        P2=Y2/greater
        if(P2!=0):
          E2-=P2*np.log2(P2)
    E1*=less/total
    E2*=greater/total
    E=E1+E2
    if(E<min_ent):
      min_ent=E
      split_length=x
  return min_ent,split_length


# In[4]:


def create_partition1(subdata,i):
  if(i==3):
    print("Dataset divided into "+str(i+1)+" datasets on the basis of above given splits")
    return subdata
  else:
    data=subdata.pop(0)
    labels=np.unique(data[:,2])
    E=0
    total=len(data)
    for x in labels:
      Y=np.count_nonzero(data[:,2]==x)
      E-=(Y/total)*np.log2(Y/total)
    min_length_entropy,min_length=entropy(data,0)
    min_width_entropy,min_width=entropy(data,1)
    length_IG=E-min_length_entropy
    width_IG=E-min_width_entropy
    if(length_IG>width_IG):
        data1=data[data[:,0]<=min_length]
        data2=data[data[:,0]>min_length]
        print("split no."+str(i+1)+" at sepal length :"+str(min_length))
        subdata.append(data1)
        subdata.append(data2)
    else:
        data1=data[data[:,1]<=min_width]
        data2=data[data[:,1]>min_width]
        print("split no."+str(i+1)+" at sepal width :"+str(min_width))
        subdata.append(data1)
        subdata.append(data2)
    return create_partition1(subdata,i+1)


# In[5]:


def plot_graph(data):
  grouped = df.groupby('class_label')
  colors = ["red", "blue","green"]
  fig, ax = plt.subplots()
  i=0
  for key, group in grouped:
      group.plot(ax=ax, kind='scatter', x='sepal_length', y='sepal_width', label=key, color=colors[i])
      i+=1
  for d in data:
    xmin=np.min(d[:,0])
    xmax=np.max(d[:,0])
    ymin=np.min(d[:,1])
    ymax=np.max(d[:,1])
    plt.plot([xmin,xmax],[ymin,ymin])
    plt.plot([xmin,xmax],[ymax,ymax])
    plt.plot([xmin,xmin],[ymin,ymax])
    plt.plot([xmax,xmax],[ymin,ymax])
  plt.show()


# In[6]:


df=pd.read_csv('train.csv')
data=df.to_numpy()
data=data[:,1:]
subdata=[]
i=0
subdata.append(data)
data1=create_partition1(subdata,i)
plot_graph(data1)

