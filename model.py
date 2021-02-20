from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.ensemble import RandomForestClassifier
import os
from sklearn.metrics import log_loss, ConfusionMatrixDisplay, average_precision_score, accuracy_score
from sklearn.metrics import roc_curve, precision_recall_curve, auc, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pickle
#def read_data(path):
#    data = pd.read_csv(path)
    #data.set_index("ID_REF",inplace = True)
    #labels = data.pop("Result")
#    return data, labels
dataset = pd.read_csv('GenesExp1.csv')
dataset.set_index("ID_REF",inplace = True)
X = dataset.iloc[:, :20]
y = dataset.iloc[:, -1]
path_model="F:/GeneModel/"
#X,y=read_data("GenesExp1.csv")
# name="Model"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=1)
model=RandomForestClassifier(criterion='gini', max_depth=6, min_samples_leaf=1, min_samples_split=2,
                       n_estimators=100)
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[11.27285579,13.11888698,13.04983865,7.160173909,11.84600012,11.38408063,12.46225539,10.35803641,10.43634604,10.31537082,8.195574032,11.00985731, 9.804574801,	7.811523898,9.271842845,8.808279933,8.473070081,8.818380484,9.115116886, 9.315489635
]]))
