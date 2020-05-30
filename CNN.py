#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Header_Section Start
from keras.layers import Convolution2D 
from keras.layers import MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.optimizers import Adam
from keras_preprocessing.image import ImageDataGenerator
#Header_Section End


# In[9]:


#Variables_Declaration Start
input_shapes=(64, 64, 3)
kernel=(3,3)
pool=(2, 2)
epoch=15
#Variables_Declaration End


# In[10]:


#NN_Model Start
model = Sequential()


# In[11]:


#Input_Layer Start
model.add(Convolution2D(filters=32, kernel_size=kernel, activation='relu',input_shape=input_shapes))
model.add(MaxPooling2D(pool_size=pool))
#Input_Layer End


# In[6]:


#CRP Start
model.add(Convolution2D(filters=32, kernel_size=kernel, activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#CRP End


# In[7]:


#Flattening Start
model.add(Flatten())
#Flattening End


# In[ ]:


#Fully_Connected Start
model.add(Dense(units=1024, activation='relu'))
model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=256, activation='relu'))
#Fully_Connected End
#Final_Layer Start
model.add(Dense(units=1, activation='sigmoid'))
#Final_Layer End


# In[ ]:


#Compiling Start
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#Compiling End


# In[ ]:


#Data_Augmentation Start
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
#Data_Augmentation End


# In[ ]:


#Model_Training Start
model.fit(training_set, epochs=epoch, validation_data=test_set, validation_steps=800)
#Model_Training End


# 
