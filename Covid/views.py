from django.shortcuts import render
from .models import FormInfo
from django.http import HttpResponse
# Create your views here.
# Added for Regression model
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


def index(request):
    if request.method == 'POST':
        name = request.POST.get('username', 'error')
        email = request.POST.get('useremail', 'error')
        phone = request.POST.get('userphone', 'error')
        fever = int(request.POST.get('Fever', 'error'))
        age = int(request.POST.get('Age', 'error'))
        pain = int(request.POST.get('Pain', 'error'))
        nose = int(request.POST.get('Nose', 'error'))
        breath = int(request.POST.get('DiffBreath', 'error'))
        cough = int(request.POST.get('Coughprob1', 'error'))
        lososa = int(request.POST.get('lososat', 'error'))
        Ddiabetic = int(request.POST.get('diabetic', 'error'))
        hytension = int(request.POST.get('hyptension', 'error'))
        lung = int(request.POST.get('ldisease', 'error'))
        heart = int(request.POST.get('heartdis', 'error'))
        kidney = int(request.POST.get('Kidneydis', 'error'))
        print(name, email, phone, fever, age, pain, nose,
              breath, hytension, lung, heart, kidney)

        if (age >= 0 and age <= 9):
            values = [fever, pain, nose, breath, cough,
                      lososa, Ddiabetic, hytension, lung, heart, kidney, 1, 0, 0, 0, 0]
        elif (age >= 10 and age <= 19):
            values = [fever, pain, nose, breath, cough,
                      lososa, Ddiabetic, hytension, lung, heart, kidney, 0, 1, 0, 0, 0]
        elif (age >= 20 and age <= 24):
            values = [fever, pain, nose, breath, cough,
                      lososa, Ddiabetic, hytension, lung, heart, kidney, 0, 0, 1, 0, 0]
        elif (age >= 25 and age <= 59):
            values = [fever, pain, nose, breath, cough,
                      lososa, Ddiabetic, hytension, lung, heart, kidney, 0, 0, 0, 1, 0]
        else:

            values = [fever, pain, nose, breath, cough, lososa,
                      Ddiabetic, hytension, lung, heart, kidney, 0, 0, 0, 0, 1]

        final_prob = getproba(values)
        user_info = FormInfo(name=name, email=email, phone=phone, fever_value=fever, age=age, body_pain=pain, runnyrose=nose, diff_breath=breath, coughprob=cough,
                             lososat=lososa, diabetic_patient=Ddiabetic, hypertension_prob=hytension, lung_disease=lung, heart_disease=heart, kidney_disease=kidney)
        user_info.save()

        final_prob = round(final_prob)
        return render(request, 'covid/show.html', {'proba': final_prob})

    return render(request, 'covid/index.html')


def getproba(values):

    data = pd.read_csv('Covid/static/final_data.csv')
    train, test = data_split(data, 0.33)
    X_train = train[['Fiver', 'Bodypain', 'RunnuNose', 'BreathingProb', 'CoughProb', 'LOSOFAT', 'Diabetes', 'Hypertension',
                     'Lung Disease', 'Heart Disease', 'KidneyDisorder', 'Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+']].to_numpy()
    X_test = test[['Fiver', 'Bodypain', 'RunnuNose', 'BreathingProb', 'CoughProb', 'LOSOFAT', 'Diabetes', 'Hypertension',
                   'Lung Disease', 'Heart Disease', 'KidneyDisorder', 'Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+']].to_numpy()
    y_train = train[['InfectionProbablity']].to_numpy().reshape(21226, )
    y_test = test[['InfectionProbablity']].to_numpy().reshape(10454, )
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    probablity_info = clf.predict_proba([values])[0][1]*100
    return probablity_info


def data_split(data, ratio):
    np.random.seed(40)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_data = shuffled[:test_set_size]
    train_data = shuffled[test_set_size:]
    return data.iloc[train_data], data.iloc[test_data]


def show(request):
    return HttpResponse('Show Page')
