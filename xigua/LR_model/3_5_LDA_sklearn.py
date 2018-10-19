import pandas as pd
import numpy as np

input_file="xg3.csv"
ori_data=pd.read_csv(input_file)
X=np.array([list(ori_data['density']),list(ori_data['suger']),[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
y=list(ori_data['good'])
X=X.T
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import metrics
import matplotlib.pyplot as plt

# generalization of train and test set
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=0)

# model fitting
lda_model = LinearDiscriminantAnalysis(solver='lsqr', shrinkage=None).fit(X_train, y_train)

# model validation
y_pred = lda_model.predict(X_test)

# summarize the fit of the model
print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))
