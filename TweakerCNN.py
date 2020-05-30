#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import listdir
from os.path import isfile, join
import sys
data_path="/gitfiles/"
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
path="/gitfiles/{0}".format(i)


# In[1]:


def condition1():#Adding 1 CRP layers
    s=open(path)
    code=s.read()
    s.close()
    st=code.split('\n')
    if '#CRP Start' in st and '#CRP End' in st:
        print("true")
        s2=st[st.index('#CRP Start')+1:st.index('#CRP End')]
        print(s2)
        if(len(s2)==2):
            s2.append(s2[0])
            s2.append(s2[1])
            s2.append(s2[0])
            s2.append(s2[1])
        elif (len(s2)==3):
            s2.append(s2[0])
            s2.append(s2[1])
            s2.append(s2[2])
        else:
            s2.append(s2[0])
            s2.append(s2[1])
        st1=st[0:st.index('#CRP Start')+1]+s2+st[st.index('#CRP End'):]
        st1=str('\n'.join(st1))
        print(st1)
        w=open(path,'w')
        w.write(st1)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[2]:


def condition2():#Changing number of epochs
    s=open(path)
    code=s.read()
    s.close()
    dat=code.split('\n')
    if '#Variables_Declaration Start' in dat and '#Variables_Declaration End' in dat:
        s5=dat[dat.index('#Variables_Declaration Start')+1:dat.index('#Variables_Declaration End')]
        s5
        for i in range(len(s5)):
            if "epoch" in s5[i]:
                temp=s5[i].split("=")
                art=0
                val=int(temp[-1])
                if val<=20:
                    val=20
                else:
                    val+=15
                temp[-1]=str(val)
                s5[i]=str('='.join(temp))
        dat=dat[0:dat.index('#Variables_Declaration Start')+1]+s5+dat[dat.index('#Variables_Declaration End'):]
        print(dat)
        dat=str('\n'.join(dat))
        print(dat)
        w=open(path,'w')
        w.write(dat)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[4]:


def condition3():#Adding 2 more FC layers
    s=open(path)
    code=s.read()
    s.close()
    st=code.split('\n')
    if '#Fully_Connected Start' in st and '#Fully_Connected End' in st:
        print("true")
        s2=st[st.index('#Fully_Connected Start')+1:st.index('#Fully_Connected End')]
        print(s2)
        s2.append(s2[-1])
        s2.append(s2[-1])
        st1=st[0:st.index('#Fully_Connected Start')+1]+s2+st[st.index('#Fully_Connected End'):]
        st1=str('\n'.join(st1))
        print(st1)
        w=open(path,'w')
        w.write(st1)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[5]:


def condition4():#Decreasing number of neurons in hidden layers in a pattern
    s=open(path)
    code=s.read()
    s.close()
    dat=code.split('\n')
    if '#Variables_Declaration Start' in st and '#Variables_Declaration End' in st:
        s3=dat[dat.index('#Variables_Declaration Start')+1:dat.index('#Variables_Declaration End')]
        for i in range(len(s3)):
            if "kernel" in s3[i]:
                temp=s3[i].split("=")
                temp[-1]='(4,4)'
                s3[i]=str('='.join(temp))
                break
        dat=dat[0:dat.index('#Variables_Declaration Start')+1]+s3+dat[dat.index('#Variables_Declaration End'):]
        print(dat)
        w=open(path,'w')
        w.write(dat)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[6]:


value=sys.argv[1]
if value=='1':
    condition1()
elif value=='2':
    condition2()
elif value=='3':
    condition3()
elif value=='4':
    condition4()


# In[ ]:




