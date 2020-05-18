from flask import render_template, jsonify, request
from app import app
import io
import os
import cv2
#from google.cloud import vision_vlp3betal as vision_vlp3betal
from datetime import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
import pandas as pd

@app.route('/example')
def example():
    URL = 'https://api.openweathermap.org/data/2.5/'
    key = 'b1ffe3330b6cdb03e70a9e5842a7f0b1'
    return render_template('example.html', API_URL=URL, API_KEY=key)

@app.route('/api/diabetes_prediction', methods=['POST'])
def diabetes():
    pregnant = request.json['pregnant']
    glucose = request.json['glucase']
    skin = request.json['skin']
    insul = request.json['insulin']
    imc = request.json['imc']
    blood = request.json['blood']
    age = request.json['age']

    diabetes_data = pd.read_csv("./routes/diabet/diabetes.csv")
    diabetes_data.head()

    diabetes_data[:60]
    diabetes_data.shape

    diabetes_data.isna().sum()
    diabetes_data.dtypes

    X = diabetes_data.drop("Outcome", axis=1)
    y = diabetes_data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    svc_model = LinearSVC(max_iter=10000)
    svc_model.fit(X_train, y_train)

    svc_score = svc_model.score(X_test, y_test)
    if svc_score < 0.6:
        print(f"SVC Model Score is Less: {svc_score}".format())
    else:
        random_clf = RandomForestClassifier(n_estimators=100, ccp_alpha=0.0)
        random_clf.fit(X_train, y_train)
        #skljson.to_json(random_clf, "../../ModelDiabete")
        #deserialized_model = skljson.from_json("ModelDiabete")
        X = np.array([[pregnant, glucose, blood, skin, insul, imc, 0.3, age]])
        prediction = random_clf.predict(X)
    return jsonify(prediction.tolist())
