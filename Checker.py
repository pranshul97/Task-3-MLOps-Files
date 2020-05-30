#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import listdir
from os.path import isfile, join
data_path="/root/gitfiles/"
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
print(i)
path="/root/gitfiles/{0}".format(i)


# In[2]:


#Header Part
s=open(path)
code=s.read()
s.close()
st=code.split('\n')
#print(st)
if '#Header_Section End' in st:
    #print("true")
    s1=st[st.index('#Header_Section Start')+1:st.index('#Header_Section End')]
    cnn=0
    ann=0
    kmeans=0
    for i in s1:
        if (('Convolution' in i) or ('Pooling' in i)):
            print("CNN")
            cnn=1
    if cnn==0:
        for i in s1:
            if ('Sequential' in i) or ('Dense' in i):
                print("ANN")
                ann=1
    if ann==0 and cnn==0:
        for i in s1:
            if ('KMeans' in i):
                kmeans=1
                print("KMeans")


# In[ ]:




