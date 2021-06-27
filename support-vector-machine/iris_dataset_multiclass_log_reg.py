# -*- coding: utf-8 -*-
"""iris-dataset_multiclass_log_reg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fE5_PB057j4fdcsPuTbme-zJk-CEJ8C1
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.datasets import load_iris
# %matplotlib inline
import matplotlib.pyplot as plt
iris = load_iris()

dir(iris)

print (iris.feature_names)

print(iris.target_names)

iris.data[0]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target, test_size=0.2)



model.fit(X_train, y_train)

model.score(X_test,y_test)

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm

import seaborn as sn
plt.figure(figsize = (7,5))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
