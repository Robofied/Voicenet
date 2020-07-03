## Importing libraries


## Built-in python package
import numpy as np
import pandas as pd
import os, sys, wave
import logging


from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score


## Our-defined packages
from voicenet.utils import basic_utils, download
from voicenet.utils.features_extraction import mfcc_features
from voicenet.training import SplitData

"""Setup"""
# logger setup
basic_utils.setup_logging()
logger = logging.getLogger(__name__)

## GLOBAL VARIABLES
STAEDS = 'ST-AEDS'

class GMMModelTraining:
    
    def __init__(self, staeds_flag=True):  
        
        self.staeds_flag = staeds_flag        

    def collect_features(self, files_list):
        
        features = np.asarray(())
        
        for file in files_list:
            
            logger.info("Creating features for {0}".format(file))
            
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
            
            logger.info("Working on STAEDS data")
            
            download.download_staeds_extract_data(data_dir)
            SplitData.staeds_training_data_preparation(os.path.join(data_dir, STAEDS))

            females, males = basic_utils.get_file_paths(os.path.join(data_dir, STAEDS,'TrainingData/females'), os.path.join(data_dir, STAEDS,'TrainingData/males') )

        ## else: need to split download and split data in not staeds
        
        else:
            
            
        
            
        # logger.info(females, males)

        female_mfcc_features = self.collect_features(females)
        male_mfcc_features = self.collect_features(males)

        # print(female_mfcc_features)
        
        logger.info("Fitting GMM Model for females and males")

        females_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)
        males_gmm = GaussianMixture(n_components = 16, max_iter = 200, covariance_type = 'diag', n_init = 3)

        # fit features to models
        females_gmm.fit(female_mfcc_features)
        males_gmm.fit(male_mfcc_features)

        basic_utils.save_gmm_model(females_gmm, os.path.join(model_dir,'females_gmm_model'))
        basic_utils.save_gmm_model(males_gmm, os.path.join(model_dir,'males_gmm_model'))
        
        
        
        
        

        
            
        



