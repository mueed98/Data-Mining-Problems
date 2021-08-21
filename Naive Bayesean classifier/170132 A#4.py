# -*- coding: utf-8 -*-

"""## Naive Bayesian"""

from matplotlib import pyplot
from pandas import DataFrame
import numpy as np
import math
import pandas as pd
import random
import copy
import random
import matplotlib.pyplot as plt
from scipy import stats

Color = []
Type = []
Origin = []
Stolen = []

df=pd.read_csv('Dataset.csv')
data=df.to_numpy()
data_rows = df.shape[0]

for i in range ( data_rows ) :
  Color.append(data[i][0])
  Type.append(data[i][1])
  Origin.append(data[i][2])
  Stolen.append(data[i][3])

data = []
data.append ( Color )
data.append ( Type )
data.append ( Origin )
data.append ( Stolen )



def getSingleProb( a ):
  a_row = 0
  for i in range ( len(data) ) :
      if a in data[i]:
        a_row = i
  
  count_a = 0

  for i in range ( len(data[a_row]) ) :
    if data[a_row][i] == a :
        count_a += 1

  print ("P (", a , ")" , "=" , count_a, "/", len(data[a_row]),  "=" , count_a/len(data[a_row]) )

  return count_a/len(data[a_row])

# prob of x given y
def getProb ( a , b ) :
  a_row = 0
  b_row = 0
  for i in range ( len(data) ) :
      if a in data[i]:
        a_row = i
      if b in data[i]:
        b_row = i
  
  count_a = 0
  count_b = 0

  for i in range ( len(data[a_row]) ) :
    if data[a_row][i] == a :
      if data[b_row][i] == b :
        count_a += 1

  for i in range ( len(data[b_row]) ) :
      if data[b_row][i] == b :
        count_b += 1

  print ("P (", a , "/" , b , ")" , "=" , count_a, "/", count_b, "=" , count_a/count_b )

  return count_a/count_b



def process ( ColorGiven, TypeGiven, OriginGiven) :
    yes_prob = []
    yes_prob.append ( getProb (ColorGiven,"Yes") )
    yes_prob.append ( getProb (TypeGiven,"Yes") )
    yes_prob.append ( getProb (OriginGiven,"Yes") )

    no_prob = []
    no_prob.append ( getProb (ColorGiven,"No") )
    no_prob.append ( getProb (TypeGiven,"No") )
    no_prob.append ( getProb (OriginGiven,"No") )

    P_X_yes = np.prod ( yes_prob )
    P_X_no = np.prod ( no_prob )

    P_X_prob = []
    P_X_prob.append ( getSingleProb (ColorGiven) )
    P_X_prob.append ( getSingleProb (TypeGiven) )
    P_X_prob.append ( getSingleProb (OriginGiven) )

    P_X_All = np.prod ( P_X_prob )

    P_X_yes =  P_X_yes / P_X_All
    P_X_no  = P_X_no / P_X_All


    if P_X_no > P_X_yes :
      print ("Stolen = No " )
    else:
      print ("Stolen = Yes " )

# --------- THIS IS MAIN PART ----------
# --------- SET THE VARIABLES HERE -----------
# --------- CODE IS GENERIC -----------

Color  = "Yellow"
Type  = "SUV"
Origin = "Imported"

process (Color, Type, Origin)