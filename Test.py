# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:33:43 2018

@author: Satheesh Reddy
"""

import os
import pandas as pd
from sklearn import preprocessing, tree, neighbors, metrics, linear_model
from sklearn_pandas import DataFrameMapper,CategoricalImputer
import numpy as np
from sklearn import model_selection, ensemble
import seaborn as sns
from sklearn import feature_selection
import math
from mlxtend import regressor

#changes working directory
#path = 'D:/DSSensors/'
#Sensors_train = pd.read_csv(os.path.join(path,"Train.csv"))
#Sensors_train.shape
#Sensors_train.info()
#caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
#other = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
#caller.info()
#other.info()
#caller.join(other, lsuffix='_caller', rsuffix='_other')
#caller.set_index('key').join(other.set_index('key'))
#caller.join(other.set_index('key'), on='key')


path = 'D:/DSSensors/Data/'  
Sensors_train = pd.read_csv(os.path.join(path,"Train.csv"))
Sensors_train.shape
Sensors_train.info()
Sensors_train.set_index('Time')
Sensors_train2 = pd.read_csv(os.path.join(path,"Train_event_val.csv"))#Train_event_val
Sensors_train2.shape
Sensors_train2.info()
Sensors_train2.set_index('Time')

#Sensors_train3=Sensors_train.set_index('Time').join(Sensors_train2.set_index('Time'))
Sensors_train4=Sensors_train.join(Sensors_train2.set_index('Time'), on='Time')
Sensors_train4
