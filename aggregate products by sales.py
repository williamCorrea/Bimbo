# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 13:24:23 2016

@author: correabe
"""
import matplotlib.pyplot as plt
import sys
from numpy import random
import matplotlib
import pandas as pd
import os

#I specify that some columns are of str type in order to use the function describe()
#fixed_df = pd.read_csv("D:/kaggle/Bimbo/test.csv")
fixed_df = pd.read_csv("D:/kaggle/Bimbo/sub_train/train0.csv",
                    dtype={'Semana':str,'Cliente_ID':str})

Productos = fixed_df.groupby(['Producto_ID','Semana'])
Pr_sum = Productos.sum()
Pro2 =Pr_sum.sort(['Venta_uni_hoy'],ascending=False)
otro =Pro2.loc[:,['Venta_uni_hoy','Dev_uni_proxima']]


fichiers = os.listdir('D:/kaggle/Bimbo/sub_train/')
#print type(fichiers)
for i in fichiers:
        
    if i!="train0.csv":
        otro_2 = pd.read_csv('D:/kaggle/Bimbo/sub_train/'+str(i),
                    dtype={'Semana':str,'Cliente_ID':str})
        Productos_2 = otro_2.groupby(['Producto_ID','Semana'])
        Pr_sum_2 = Productos_2.sum()
        Summary = Pr_sum_2.loc[:,['Venta_uni_hoy','Dev_uni_proxima']]            
            
        temp=[otro,Summary]
        otro=pd.concat(temp)

print otro.info()

otro.to_csv("D:/kaggle/Bimbo/summary.csv")






#Pro2[:500]['Venta_uni_hoy'].plot()

#fixed_df['Venta_uni_hoy'].plot(kind='bar')