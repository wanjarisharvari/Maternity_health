import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix 
from sklearn.ensemble import RandomForestClassifier




# high risk = 2, midrisk = 1, lowrisk = 0 
df= pd.read_csv('risk_data.csv')
#print(df.columns)
# 'Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate', 'RiskLevel'
#df.plot(kind = 'bar', x= '', y='')
# Visualize the whole dataset

#df.groupby('RiskLevel').size()
#df.describe()





X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=0)

#X_train = st_x.fit_transform(X_train)
#X_test = st_x.transform(X_test)
#st_x = StandardScaler()

'''log_reg = LogisticRegression()
log_reg.fit(X_train,Y_train)
 

Y_pred = log_reg.predict(X_test)'''


#plt.scatter(X_test,Y_test)
#plt.plot(X_test,test_pred)
#X_new = np.linspace(0,3,1000).reshape(-1,1)

'''model = SVC(kernel =  'poly' , random_state=0)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)'''

model = RandomForestClassifier()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
#plt.scatter(X_test[:,1],Y_test)
#plt.plot(X_test[:,1],Y_pred) 
cm= confusion_matrix(Y_test, Y_pred)  
#print(cm)
plt.show()
a= np.zeros(shape=(1,6))
input("hi")
a[0]=input("Age")
a[1]=input("sbp")
a[2]=input("dbp")
a[3]=input("bs")
a[4]=input("temp")
a[5]=input("rate")
print(model.predict(a))


