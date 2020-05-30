#!/usr/bin/env python
# coding: utf-8
#Header_Section Start
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
#Header_Section End
#Data_Reading Start
dataset = pd.read_csv('Example.csv')
#Data_Reading End
#Variable_Declaration Start
wcss=[]
n_cluster=3
#Variable_Declaration End
#Scaling Start
sc = StandardScaler()
dataset = sc.fit_transform(dataset)
#Scaling End
#Model_Creation Start
model = KMeans(n_clusters=n_cluster)
pred  = model.fit_predict(dataset)
#Model_Creation End
#Printing_Result Start
print("Clusters=",n_cluster)
print(pred)
#Printing_Result End