# For Importing Files
import os
import sys
import math
import tarfile

# For Data Manipulation
import numpy as np
import pandas as pd

# For Audio Files Processing
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM
from python_speech_features import mfcc
from python_speech_features import delta 
from sklearn import preprocessing

# To Ignore Warnings
import warnings
warnings.filterwarnings('ignore')

# To Save Models
import pickle

#preprocess
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer,LabelEncoder,OneHotEncoder
from Features_Extractor import Features_Extractor
import Data_Manager

class Models_Trainer:
    
    # Function #1
    
    def __init__(self, females_files_path, males_files_path):
        self.females_training_path = females_files_path
        self.males_training_path   = males_files_path
        self.features_extractor    = Features_Extractor()
#-----------------------------------------------------------------------------------------------------------------------------        
    
    # Function #2
    
    def get_file_paths(self, females_training_path, males_training_path):
        females = [ os.path.join(females_training_path, f) for f in os.listdir(females_training_path) ]
        males   = [ os.path.join(males_training_path, f) for f in os.listdir(males_training_path) ]
        return females, males
    
#-----------------------------------------------------------------------------------------------------------------------------
    
    # Function #3  
    
    def collect_features(self, files):
        features = np.asarray(())
        
        for file in files:
            print("%5s %10s" % ("Processing ", file))
            vector = self.features_extractor.extract_features(file)
            if features.size == 0: 
                features = vector
            else:
                features = np.vstack((features, vector))
        return features
    
#------------------------------------------------------------------------------------------------------------------------------ 
    # Function #4
    
    def process(self):
        females, males = self.get_file_paths(self.females_training_path,self.males_training_path)
        
        female_voice_features = self.collect_features(females)
        male_voice_features   = self.collect_features(males)
        
        females_gmm = GMM(n_components = 16, max_iter = 200, covariance_type='diag', n_init = 3)
        males_gmm   = GMM(n_components = 16, max_iter = 200, covariance_type='diag', n_init = 3)
        
        females_gmm.fit(female_voice_features)
        males_gmm.fit(male_voice_features)
        
        self.save_gmm(females_gmm, "females")
        self.save_gmm(males_gmm,   "males")

#-----------------------------------------------------------------------------------------------------------------------------
    # Function #5
    
    def save_gmm(self, gmm, name):

        filename = name + ".gmm"
        
        with open(filename, 'wb') as gmm_file:
            pickle.dump(gmm, gmm_file)
        print ("%5s %10s" % ("Saving", filename,))

#-----------------------------------------------------------------------------------------------------------------------------
if __name__== "__main__":
    models_trainer = Models_Trainer("TrainingData/females", "TrainingData/males")
    models_trainer.process()
    
