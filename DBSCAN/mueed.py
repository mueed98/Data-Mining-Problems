# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 00:58:33 2021

@author: Mueed i170132

"""

from sklearn.datasets import make_moons
from matplotlib import pyplot
from pandas import DataFrame
import numpy as np
import pandas as pd
import random
import copy


def distance(p1,p2):
  dist=pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2)
  return dist**0.5

def DBscanRunner(data,eps,minP):
  points=[]     #handles all points
  clusters=[[]] #cluster growth queue
  outliers=[]   # handles outliers
  points.append(data[0])
  labels=0
  data[0][3]=True
  while(points):
    p1=points.pop(0)
    labelcount=np.zeros(100)
    closepoints=0
    for p2 in data:
      if(distance(p1,p2)<=eps): # checking for neighbours
        closepoints+=1
        if(p2[3]==False):
          points.append(p2)
          p2[3]=True
        if(p2[2]!=0):
          labelcount[p2[2]]+=1
    if(closepoints>=minP):
      if(labelcount.sum()==0):  # assigns a label if no label was given already
          labels+=1     
          p1[2]=labels
          clusters.append([])
          clusters[labels].append(p1)
      else: 
          p1[2]=np.argmax(labelcount)
          clusters.append([])
          clusters[p1[2]].append(p1)
    else:
      outliers.append(p1)
          
    if(not(points)):
      for p in data:
        if(p[3]==False):
          points.append(p)
          break
  return clusters,outliers
        

def DBSCAN(data1, eps,minP) :
    data = copy.deepcopy(data1) 
    clusters,outliers=DBscanRunner(data,eps,minP)
    for cluster in clusters:
      cluster=np.array(cluster)
      if(cluster.any()):
        pyplot.plot(cluster[:,0], cluster[:,1],'o', label = "Cluster")
    outliers=np.array(outliers)
    if(outliers.any()):
      pyplot.plot(outliers[:,0], outliers[:,1],'o', label = "Outliers")
    pyplot.legend()
    pyplot.title("Output at Eps = "+str(eps)+" and MinP = "+str(minP) )
    pyplot.show()



# MAIN

df=pd.read_csv('moonDataset.csv')
df['visited']=False
data=df.to_numpy()
DBSCAN(data,0.05,10)    # Low epsilon high min points
DBSCAN(data,0.2,6)    # Neither strict nor relaxed
DBSCAN(data,0.8,3)    # High epsilon low min points