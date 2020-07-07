import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import LabelEncoder
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import sys
import wave
from scipy.io.wavfile import read
from python_speech_features import delta 
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score

#Custom Function Imports
from getmfcc import GetMfcc

DATA_RAW_DIR = '../data/ST-AEDS'

# Create the pandas DataFrame 
df = pd.DataFrame(columns = ['path', 'gender']) 

male_list = []
female_list = []
for filename in os.listdir(DATA_RAW_DIR):
    if filename.startswith("m"):
        male_list.append(os.path.join(DATA_RAW_DIR, filename))
    if filename.startswith("f"):
        female_list.append(os.path.join(DATA_RAW_DIR, filename))

for i in range(len(male_list)):
    df = df.append({'path' : male_list[i] , 'gender' : 'male'} , ignore_index=True)

for i in range(len(female_list)):
    df = df.append({'path' : female_list[i] , 'gender' : 'female'} , ignore_index=True)
    
le = LabelEncoder()
le.fit(df['gender'])
df['gender'] = le.transform(df['gender'])
df['mfcc'] = ''

for i in range(len(df['path'])):
    df['mfcc'][i]= get_mfcc(df['path'][i]) 
    
max_length = np.amax(df['len'])
print("Max length of MFCC is: ", str(max_length))

zeros_array = np.zeros((max_length, 39))
# df['mfcc'][1] = np.append(df['mfcc'][1],data)
# zeros_array.shape

for i, row in df.iterrows():
    zeros_array[:row['mfcc'].shape[0], :row['mfcc'].shape[1]] = row['mfcc']
    df.at[i, 'mfcc'] = zeros_array
    
df['mfcc'] = df['mfcc'].apply(lambda x: x.ravel())

X_train, X_test, y_train, y_test = train_test_split(df['mfcc'], df['gender'], test_size=0.33, random_state=42)
print(len(X_train),len(y_train))
    
features = np.asarray(())
for i, vector in enumerate(X_train):
    if features.size == 0: 
        features = vector
    else:
        features = np.vstack((features, vector))

features_test = np.asarray(())
for i, vector in enumerate(X_test):
    if features_test.size == 0: 
        features_test = vector
    else:
        features_test = np.vstack((features_test, vector))
        
y_train = np.array(y_train)
X_train = np.array(X_train)



'''

np.reshape(X_train[0],(1,38961)).shape
y_train = np.array(y_train)
y_train = y_train.reshape(-1,1)
np.array(X_train)[0].flatten().shape
X_train = np.array(X_train).flatten()
# print(np.array(X_train).flatten())

X_train  = np.array(X_train).flatten
gmm_model = GaussianMixture(n_components=2).fit(features, y_train)
print(gmm_model.score(X_test[0]))

print(accuracy_score(np.array(y_test), prediction))

            
'''    