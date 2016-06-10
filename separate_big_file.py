# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:34:00 2016

@author: correabe
"""

import pandas as pd

#destinations = pd.read_csv("D:/kaggle/Bimbo/train.csv")
#test = pd.read_csv("test/test.csv")
#train = pd.read_csv("train/train.csv")

#print destinations.shape

with open('D:/kaggle/Bimbo/train.csv') as f:
   i=1
   archivo=0
   fo = open("D:/kaggle/Bimbo/sub_train/train"+str(archivo)+".csv","w")
   header=f.readline()
   fo.write(header)
   for line in f:
        if (i % 500000==0):       
            archivo+=1
            fo.close()
            fo = open("D:/kaggle/Bimbo/sub_train/train"+str(archivo)+".csv","w")
            fo.write(header)
        else:
            fo.write(line)
        i+=1
   fo.close()



"""
    for i in range(0,100):
        content = f.readline()
        print content
        i+=1
"""