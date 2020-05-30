#!/usr/bin/env python
# coding: utf-8

# In[6]:


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


# In[7]:


def condition1():#Adding 2 hidden layers
    s=open(path)
    code=s.read()
    s.close()
    st=code.split('\n')
    if '#Hidden_Layers Start' in st and '#Hidden_Layers End' in st:
        print("true")
        s2=st[st.index('#Hidden_Layers Start')+1:st.index('#Hidden_Layers End')]
        print(s2)
        if(len(s2)==1):
            s2.append(s2[0])
            s2.append(s2[0])
        else:
            s2.append(s2[0])
            s2.append(s2[0])
        st1=st[0:st.index('#Hidden_Layers Start')+1]+s2+st[st.index('#Hidden_Layers End'):]
        st1=str('\n'.join(st1))
        print(st1)
        w=open(path,'w')
        w.write(st1)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[8]:


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
                if val<=50:
                    val=100
                else:
                    val+=50
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


# In[9]:


def condition3():#Adding 2 more hidden layers
    s=open(path)
    code=s.read()
    s.close()
    st=code.split('\n')
    if '#Hidden_Layers Start' in st and '#Hidden_Layers End' in st:
        print("true")
        s2=st[st.index('#Hidden_Layers Start')+1:st.index('#Hidden_Layers End')]
        print(s2)
        s2.append(s2[-1])
        s2.append(s2[-1])
        st1=st[0:st.index('#Hidden_Layers Start')+1]+s2+st[st.index('#Hidden_Layers End'):]
        st1=str('\n'.join(st1))
        print(st1)
        w=open(path,'w')
        w.write(st1)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[10]:


def condition4():#Decreasing number of neurons in hidden layers in a pattern
    s=open(path)
    code=s.read()
    s.close()
    dat=code.split('\n')
    if '#Hidden_Layers Start' in st and '#Hidden_Layers End' in st:
        s5=dat[dat.index('#Variables_Declaration Start')+1:dat.index('#Variables_Declaration End')]
        for i in range(len(s5)):
            if "input_dims" in s5[i]:
                temp=s5[i].split("=")
                art=0
                val=int(temp[-1])
                if (val-(2*len(s4))>10):
                    alert=0
                else:
                    alert=1
        s3=dat[dat.index('#Variables_Declaration Start')+1:dat.index('#Variables_Declaration End')]
        for i in range(len(s3)):
            if "neurons" in s3[i]:
                temp=s3[i].split("=")
                art=0
                for j in range(len(s3)):
                    if 'input_dims' in s3[j]:
                        art=1
                if art==1:
                    temp[-1]='input_dims'
                    s3[i]=str('='.join(temp))
        dat=dat[0:dat.index('#Variables_Declaration Start')+1]+s3+dat[dat.index('#Variables_Declaration End'):]
        print(dat)
        s4=dat[st.index('#Hidden_Layers Start')+1:dat.index('#Hidden_Layers End')]
        if alert==0:
            c=0
            for i in range(len(s4)):
                print(s4[i])
                c+=1
                ll=s4[i].index('units=neurons')
                s4[i]=s4[i][0:29]+str(-(c*2))+s4[i][29:-1]
        else:
            c=0
            for i in range(len(s4)):
                print(s4[i])
                c+=1
                ll=s4[i].index('units=neurons')
                s4[i]=s4[i][0:29]+str(-(c))+s4[i][29:-1]
        print(s4)
        dat=dat[0:dat.index('#Hidden_Layers Start')+1]+s4+dat[dat.index('#Hidden_Layers End'):]
        dat=str('\n'.join(dat))
        print(dat)
        w=open(path,'w')
        w.write(dat)
        w.close()
    else:
        print("wrong syntax")
        exit(1)


# In[11]:


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




