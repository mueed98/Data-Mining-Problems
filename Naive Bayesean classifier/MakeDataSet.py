
"""170132 -DM B - A#4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MoXKeJdvFZk5DMI7QcjRUt_ohjYYtkpg

## Make Data Set
"""

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


Color = ['Red','Red','Red','Yellow','Yellow','Yellow','Yellow','Yellow','Red','Red']
Type = ['Sports','Sports','Sports','Sports','Sports','SUV','SUV','SUV','SUV','Sports']
Origin = ['Domestic','Domestic','Domestic','Domestic','Imported','Imported','Imported','Domestic','Imported','Imported']
Stolen = ['Yes','No','Yes','No','Yes','No','Yes','No','No','Yes']

df = DataFrame(dict(Color=Color[:], Type=Type[:], Origin = Origin[:], Stolen = Stolen[:]))
df.to_csv('Dataset.csv', index = False, header=True)