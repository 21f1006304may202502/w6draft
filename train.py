import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
#from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

data = pd.read_csv("iris.csv")
data.head(5)



train,test = train_test_split(data,test_size=0.4,stratify=data['species'],random_state=42)
X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
y_train = train.species
X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
y_test = test.species

params = {
  "max_depth":3,
  "random_state":1
}

mod_dt = DecisionTreeClassifier(**params)
mod_dt.fit(X_train,y_train)
y_pred = mod_dt.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)

metrics_df = pd.DataFrame({
  'Metric' : ['accuracy'],
  'Score' : [accuracy]
})
metrics_df.to_csv('metrics.csv',index=False)
joblib.dump(mod_dt, "model.joblib")
