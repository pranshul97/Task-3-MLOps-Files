#!/usr/bin/env python
# coding: utf-8
from os import listdir
from os.path import isfile, join
import sys
data_path="E:\\MLOPS & DevOps\\test1\\"
#Header Part
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
onlyfiles
check=0
for i in onlyfiles:
    print(i)
    ext=i.split(".")[-1]
    print(ext)
    if ext=='py':
        check=1
        break
#print(i)
path="E:\\MLOPS & DevOps\\test1\\{0}".format(i)
s=open(path)
code=s.read()
s.close()
st=code.split('\n')
ind=st.index('#Scaling End')+1
wcss='''#Cluster_Calculation Start
wscc=[]
for i in range(1,20):
    model = KMeans(n_clusters=i)
    #model.fit(dataset)
    pred  = model.fit_predict(dataset)
    wcss.append(model.inertia_)
for i in range(1,len(wcss)):
    diff=(wcss[i-1]-wcss[i])/(wcss[i]-wcss[i+1])
    if diff>3:
        break
n_cluster=i
#Cluster_Calculation End'''
st=st[0:ind]+wcss.split('\n')+st[ind:]
st=str('\n'.join(st))
#print(st)
w=open(path,'w')
w.write(st)
w.close()