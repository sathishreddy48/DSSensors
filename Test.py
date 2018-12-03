# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:17:04 2018

@author: v-satheg
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


path = 'D:/DSSensors/Data/'
Sensors_train = pd.read_csv(os.path.join(path,"Train_1.csv"))
Sensors_train.shape
Sensors_train.info()
Sensors_train_op = pd.read_csv(os.path.join(path,"Train_event_val_1.csv"))
Sensors_train_op.shape
Sensors_train_op.info()
#Sensors_train_op.drop(['Time'],axis=1, inplace=True)


#df['state'] = df['city'].map(city_to_state)
#Sensors_train['Event_val']=Sensors_train['Time_New'].map(Sensors_train_op)
#Sensors_train=pd.concat([Sensors_train, Sensors_train_op], axis=1, join_axes=[Sensors_train.Index])
Sensors_train=pd.merge(Sensors_train, Sensors_train_op, on=['Time_New'])
Sensors_train.shape
Sensors_train.info()
#Sensors_train.drop(['Unnamed: 7'])
#set date as index

#plot data
fig, ax = plt.subplots(figsize=(30,9))
Sensors_train.head(1000).plot(ax=ax)
#Sensors_train.head(1000).plot()
ax.set_xlabel('Time_New')
plt.figure()
#Sensors_train.plot(subplots=True, figsize=(6, 6));


