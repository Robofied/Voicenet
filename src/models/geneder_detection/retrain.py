import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the necessary modelling algos.
from sklearn.linear_model import LogisticRegression
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


class retrain:
    def LogisticRegression(self, parameter_list):
        print("inside Logistic Regression")

    def KNeighborsClassifier(self, parameter_list):
        print("inside KNeighborsClassifier")

    def SVC(self, parameter_list):
            print("inside KNeighborsClassifier")

    def RandomForestClassifier(self, parameter_list):
            print("inside RandomForestClassifier")

    def GradientBoostingClassifier(self, parameter_list):
            print("inside GradientBoostingClassifier")        

    def GaussianNB(self, parameter_list):
            print("inside GaussianNB")

