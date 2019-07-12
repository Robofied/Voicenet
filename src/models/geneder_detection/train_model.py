import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the necessary modelling algos.
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB

#model selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,roc_auc_score
from sklearn.model_selection import GridSearchCV

#preprocess.
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer,LabelEncoder,OneHotEncoder

data1 = pd.read_csv("voice.csv")
data = pd.read_csv("voice.csv")
# data = data.drop(['skew','kurt','mindom','maxdom'],axis=1,inplace=True)

scaler=StandardScaler()
scaled_df= scaler.fit_transform(data.drop('label',axis=1))
X=scaled_df
Y=data1['label'].as_matrix()
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

clf_lr=LogisticRegression()
clf_lr.fit(x_train,y_train)
pred=clf_lr.predict(x_test)
print("Logistic Regression: ", accuracy_score(pred,y_test))

clf_knn=KNeighborsClassifier()
clf_knn.fit(x_train,y_train)
pred=clf_knn.predict(x_test)
print("K Nearset Neighbor: ",accuracy_score(pred,y_test))

clf_svm=SVC(kernel='rbf')
clf_svm.fit(x_train,y_train)
pred=clf_svm.predict(x_test)
print("SVC: ",accuracy_score(pred,y_test))

clf_dt=DecisionTreeClassifier()
clf_dt.fit(x_train,y_train)
pred=clf_dt.predict(x_test)
print("Decision Tree: ",accuracy_score(pred,y_test))

clf_rf=RandomForestClassifier()
clf_rf.fit(x_train,y_train)
pred=clf_rf.predict(x_test)
print("Random Forests: ", accuracy_score(pred,y_test))

clf_gb=GradientBoostingClassifier()
clf_gb.fit(x_train,y_train)
pred=clf_gb.predict(x_test)
print("Gradient Boosting: ", accuracy_score(pred,y_test))