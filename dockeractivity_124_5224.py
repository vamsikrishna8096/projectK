# -*- coding: utf-8 -*-
"""dockeractivity_124_5224.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p-v_wx810sv01YZWJa_-KqZN-EPqxWBf

###importing required libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("/content/drive/MyDrive/docker and jenkins activity/BankNote_Authentication.csv")

data

data.head()

data.tail()

data.columns

"""### Type Conversion"""

data.dtypes

data["class"] = data["class"].astype('category')

num_attr = data.select_dtypes(["float64"]).columns

data.dtypes

data.info()

data.describe()

data.nunique()

data.value_counts()

data.isnull().sum()

data.value_counts("class")

from sklearn.model_selection import train_test_split

X=data.drop(['class'],axis=1)
y=data['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=123,stratify=y)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

X.head()

y.head()

"""### Model Building"""

from sklearn.ensemble import RandomForestClassifier

classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)

score

pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

classifier.predict([[2,3,4,1]])

