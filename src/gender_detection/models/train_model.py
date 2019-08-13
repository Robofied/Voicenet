# Author1: Akshat Gupta 
# Author2: Ridhima Garg

#import basic libraries for file loading and numerical computation
##################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##################################################################

#import the necessary modelling algos.
##################################################################
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
###################################################################

#model selection
###################################################################
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,roc_curve,roc_auc_score
from sklearn.model_selection import GridSearchCV
###################################################################

#model saving
###################################################################
from sklearn.externals import joblib
###################################################################

#preprocess
###################################################################
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer,LabelEncoder,OneHotEncoder
###################################################################

#importing data from csv
###################################################################
data1 = pd.read_csv("voice.csv")
data = pd.read_csv("voice.csv")
# data = data.drop(['skew','kurt','mindom','maxdom'],axis=1,inplace=True)
###################################################################

#Standardization process
###################################################################
scaler=StandardScaler()
scaled_df= scaler.fit_transform(data.drop('label',axis=1))
X=scaled_df
Y=data1['label'].as_matrix()
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
###################################################################

# Implementation of all algorithms: Implemented algorithms are:
###############################################################
# Logistic Regression
# K Nearest Neighbor Classifier
# Decision Tree Classifier
# Random Forest Classifier
# Gradient Boosting
# Gaussian NB
###############################################################

class train:
    def LogisticRegression(self):
        print("inside Logistic Regression")
        clf_lr=LogisticRegression()
        clf_lr.fit(x_train,y_train)
        pred=clf_lr.predict(x_test)
        print("Logistic Regression: ", accuracy_score(pred,y_test))
        filename = 'LRmodel.sav'
        joblib.dump(clf_lr, filename)
        print("File Saved with name", filename)

    def KNeighborsClassifier(self):
        print("inside KNeighborsClassifier")
        clf_knn=KNeighborsClassifier()
        clf_knn.fit(x_train,y_train)
        pred=clf_knn.predict(x_test)
        print("K Nearset Neighbor: ",accuracy_score(pred,y_test))
        filename = 'KNNmodel.sav'
        joblib.dump(clf_knn, filename)
        print("File Saved with name", filename)

    def SVC(self):
            print("inside SVC")
            clf_svm=SVC(kernel='rbf')
            clf_svm.fit(x_train,y_train)
            pred=clf_svm.predict(x_test)
            print("SVC: ",accuracy_score(pred,y_test))
            filename = 'SVCmodel.sav'
            joblib.dump(clf_svm, filename)
            print("File Saved with name", filename)

    def DecisionTreeClassifier(self):
            print("inside DecisionTreeClassifier")        
            clf_dt=DecisionTreeClassifier()
            clf_dt.fit(x_train,y_train)
            pred=clf_dt.predict(x_test)
            print("Decision Tree: ",accuracy_score(pred,y_test))
            filename = 'DTmodel.sav'
            joblib.dump(clf_dt, filename)
            print("File Saved with name", filename)
        
    def RandomForestClassifier(self):
            print("inside RandomForestClassifier")
            clf_rf=RandomForestClassifier()
            clf_rf.fit(x_train,y_train)
            pred=clf_rf.predict(x_test)
            print("Random Forests: ", accuracy_score(pred,y_test))
            filename = 'RFmodel.sav'
            joblib.dump(clf_rf, filename)          
            print("File Saved with name", filename)  

    def GradientBoostingClassifier(self):
            print("inside GradientBoostingClassifier")        
            clf_gb=GradientBoostingClassifier()
            clf_gb.fit(x_train,y_train)
            pred=clf_gb.predict(x_test)
            print("Gradient Boosting: ", accuracy_score(pred,y_test))
            filename = 'GBmodel.sav'
            joblib.dump(clf_gb, filename)
            print("File Saved with name", filename)

    def GaussianNB(self):
            print("inside GaussianNB")
            clf_nb=GaussianNB()
            clf_nb.fit(x_train,y_train)
            pred=clf_nb.predict(x_test)
            print("GaussianNB: ", accuracy_score(pred,y_test))
            filename = 'NBmodel.sav'
            joblib.dump(clf_nb, filename)
            print("File Saved with name", filename)

###############################################################
# Class and functions to predict gender based on selected model
###############################################################

class predict:
    def get_gender(self, model_name):
        print("Inside get_gender")
        if model_name == "LogisticRegression":
            model_name = "LRmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "KNeighborsClassifier":
            model_name = "KNNmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "SVC":
            model_name = "SVCmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "DecisionTreeClassifier":
            model_name = "DTmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "GradientBoostingClassifier":
            model_name = "GBmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "RandomForestClassifier":
            model_name = "RFmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        elif model_name == "GaussianNB":
            model_name = "NBmodel.sav"
            loaded_model = joblib.load(model_name)
            result = loaded_model.score(x_test, y_test)
            print(result)
        
# Loading a saved model
# loaded_model = joblib.load("LRmodel.sav")
# result = loaded_model.score(x_test, y_test)
# print(result)

# Testing out the classes
# LR = train()
# LR.LogisticRegression()

#Testing class predict

x1 = predict()
x1.get_gender(model_name="LogisticRegression")

