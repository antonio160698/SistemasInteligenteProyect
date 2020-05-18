from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
import sklearn_json as skljson
import pandas as pd
import numpy as np

diabetes_data = pd.read_csv("diabetes.csv")
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
    skljson.to_json(random_clf, "../../ModelDiabete")
    #deserialized_model = skljson.from_json("ModelDiabete")
    #X_predict = np.array([[0, 137, 40, 35, 168, 43.1, 2.244, 30]])
    #deserialized_model-predict(X_predict)