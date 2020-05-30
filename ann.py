#Header_Section Start
import pandas as pd
from keras.models import Sequential
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#Header_Section End
#Data_Processing Start
dataset=pd.read_csv('/gitfiles/Churn_Modelling.csv')
geography=pd.get_dummies(dataset['Geography'],drop_first=True)
gender=pd.get_dummies(dataset['Gender'],drop_first=True)
X=dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]
X=pd.concat([X,geography,gender],axis=1)
Y=dataset['Exited']
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.20,random_state=42)
#Data_Processing End
#Variables_Declaration Start
input_dims=11
epoch=100
neurons=6
#Variables_Declaration End
#NN_Model Start
model=Sequential()
#Input_Layer Start
model.add(Dense(units=neurons, input_dim=input_dims, activation='relu' ))
#Input_Layer End
#Hidden_Layers Start
model.add(Dense(units=neurons, activation='relu'))
#Hidden_Layers End
#Model_Creation Start
model.add(Dense(units=1,  activation='sigmoid' ))
model.compile(optimizer=Adam(learning_rate=0.000001),loss='binary_crossentropy')
#Model_Creation End
#Model_Training Start
model.fit(X_train,Y_train, epochs=epoch)
#Model_Training End
#Testing Start
Y_pred=model.predict(X_test)
Y_pred.astype(int)
matrix=confusion_matrix(Y_test,Y_pred.astype(int))
#Testing End
true=matrix[0][0]+matrix[1][1]
total=true+matrix[0][1]+matrix[1][0]
accuracy=true/total
accuracy=accuracy*100
print(accuracy)