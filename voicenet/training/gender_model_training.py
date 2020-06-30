## Importing libraries

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, sys, wave
from sklearn.preprocessing import LabelEncoder

import scipy.io.wavfile as wav
from scipy.io.wavfile import read
from python_speech_features import delta 
from python_speech_features import mfcc
from python_speech_features import logfbank
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score


## Our-defined packages
from voicenet.utils import basic_utils, download
from voicenet.utils.features_extraction import mfcc_features
from voicenet.training.STAEDS_training_data_preparation import manage


# DATA_RAW_DIR = './data/raw'
# DATA_PROCESSED = './data/processed'
# MODEL_DIR = './models'
STAEDS = 'ST-AEDS'

class GMMModelTraining:
    
    def __init__(self, staeds_flag=True):  
        
        self.staeds_flag = staeds_flag        

    def collect_features(self, files_list):
        
        features = np.asarray(())
        
        for file in files_list:
            
            mfccfeatures = mfcc_features()
            vector = mfccfeatures.get_features(file)
            
            ## If features array is empty then stacking is not possible.
            if features.size == 0:
                features = vector
                
            else:
                features = np.vstack((features, vector))
                
        return features
    
    def train_model(self, data_dir, model_dir):
        
        
        if self.staeds_flag:
            
            download.download_staeds_extract_data(data_dir)
            manage(os.path.join(data_dir, STAEDS))

            females, males = basic_utils.get_file_paths(os.path.join(data_dir, STAEDS,'TrainingData/females'), os.path.join(data_dir, STAEDS,'TrainingData/males') )

        ## else: need to split download and split data in not staeds
        
        print(females, males)

        female_mfcc_features = self.collect_features(females)
        male_mfcc_features = self.collect_features(males)

        print(female_mfcc_features)

        females_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)
        males_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)

        # fit features to models
        females_gmm.fit(female_mfcc_features)
        males_gmm.fit(male_mfcc_features)

        basic_utils.save_gmm_model(females_gmm, os.path.join(model_dir,'females_gmm_model'))
        basic_utils.save_gmm_model(males_gmm, os.path.join(model_dir,'males_gmm_model'))

        
            
        
# download.download_extract_data(DATA_RAW_DIR)

# manage(os.path.join(DATA_RAW_DIR, STAEDS))

# females, males = basic_utils.get_file_paths(os.path.join(DATA_RAW_DIR, STAEDS,'TrainingData/females'), os.path.join(DATA_RAW_DIR, STAEDS,'TrainingData/males') )

# print(females, males)

# female_mfcc_features = collect_features(females)
# male_mfcc_features = collect_features(males)

# print(female_mfcc_features)

# females_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)
# males_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)

# # fit features to models
# females_gmm.fit(female_mfcc_features)
# males_gmm.fit(male_mfcc_features)

# basic_utils.save_gmm_model(females_gmm, os.path.join(MODEL_DIR,'females_gmm_model'))
# basic_utils.save_gmm_model(males_gmm, os.path.join(MODEL_DIR,'males_gmm_model'))




