## Importing libraries


## Built-in python package
import numpy as np
import pandas as pd
import os, sys, wave
import logging


from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score


## Our-defined packages
from voicenet.utils import basic_utils
from voicenet.datasets import stamerican
from voicenet.utils import FeatureExtraction
from .data_preparation import SplitData


"""Setup"""
# logger setup
basic_utils.setup_logging()
logger = logging.getLogger(__name__)

## GLOBAL VARIABLES
STAEDS = 'ST-AEDS'

class GMMModelTraining:
    
    """ Trains GMM Model 
    
        Attributes
        --------
        
        staeds_flag: If user wants to train/retrain GMM model for staeds dataset.
        
    """
    
    def __init__(self, staeds_flag=True):  
        
        self.staeds_flag = staeds_flag        

    def collect_features(self, files_list):
        
        """ Create features for all '.wav' files contains in files_list
        
        Arguments:
            files_list: takes a list of '.wav' training files

        Returns:
            features: creates a vector of all .wav training files and stack them over as an array
        """
        
        features = np.asarray(())
        
        for file in files_list:
            
            logger.info("Creating features for {0}".format(file))
            
            # mfccfeatures = mfcc_features()
            vector = FeatureExtraction.mfcc_feature(file)
            
            ## If features array is empty then stacking is not possible.
            if features.size == 0:
                features = vector
                
            else:
                features = np.vstack((features, vector))
                
        return features
    
    def train_model(self, data_dir, model_dir, data_dir_females=None, data_dir_males=None,):
        
        """ train a gmm model for data provided
        
        Arguments:
            data_dir: Splitting data from this directory for training and testing
            
            model_dir: directory where model will be saved
            
            data_dir_females: Splitting data from this directory for females for training and testing
            
            data_dir_males: Splitting data from this directory for males for training and testing
            
        Returns:
            Saved trained gmm models into model_dir
        
        
        """
        
        if self.staeds_flag:
            
            logger.info("Working on STAEDS data")
            
            # download.download_staeds_extract_data(data_dir)
            # SplitData.staeds_data_preparation(os.path.join(data_dir, STAEDS))
            stamerican(data_dir)

            females, males = basic_utils.get_file_paths(os.path.join(data_dir, STAEDS,'TrainingData/females'), os.path.join(data_dir, STAEDS,'TrainingData/males') )

        ## else: need to split download and split data in not staeds
        
        else:
            
            # SplitData.universal_data_preparation(data_dir, os.path.join(data_dir, "females"), os.path.join(data_dir,"males"))
            SplitData.universal_data_preparation(data_dir, data_dir_females, data_dir_males)
            
            females, males = basic_utils.get_file_paths(os.path.join(data_dir,'TrainingData/females'), os.path.join(data_dir,'TrainingData/males') )

            
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
        
        
        
        
        

        
            
        



