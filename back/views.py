import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import csv
# Create your views here.

@csrf_exempt
def index(request):
    csv_file_path = os.path.join('back', 'risk_data.csv')
    if request.method == 'POST':
        age = request.POST['age']
        systolicBp = request.POST['systolicBp']
        diastolicbp = request.POST['diastolicbp']
        bloodsugar = request.POST['bloodsugar']
        bodytemp = request.POST['bodytemp']
        heartrate = request.POST['heartrate']
        
        
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

        df= pd.read_csv(csv_file_path)





        X = df.iloc[:,:-1]
        Y = df.iloc[:,-1]
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=0)



        model = RandomForestClassifier()
        model.fit(X_train,Y_train)
        Y_pred = model.predict(X_test)

        cm= confusion_matrix(Y_test, Y_pred)  

        plt.show()
        print(X_train)
        a = np.zeros((1,6))
        a[0][0]=age
        a[0][1]=systolicBp
        a[0][2]=diastolicbp
        a[0][3]=bloodsugar
        a[0][4]=bodytemp
        a[0][5]=heartrate
        result=model.predict(a)
        print(result)
        if result==['high risk']:
           return render(request,'High.html')
        if result==['mid risk']:
           return render(request,'mid.html')
        else:
           return render(request,'low.html')

   

    
    return render(request,'kot.html')