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

class Gender_Identifier:
    
    # Function #1
    
    def __init__(self, females_files_path, males_files_path, females_model_path, males_model_path):
        self.females_training_path = females_files_path
        self.males_training_path   = males_files_path
        self.error                 = 0
        self.total_sample          = 0
        self.features_extractor    = Features_Extractor()
        
        self.females_gmm = pickle.load(open(females_model_path, 'rb'))
        self.males_gmm   = pickle.load(open(males_model_path, 'rb'))

#------------------------------------------------------------------------------------------------------------------------------
    
    # Function #2
    
    def get_file_paths(self, females_training_path, males_training_path):

        females = [ os.path.join(females_training_path, f) for f in os.listdir(females_training_path) ]
        males   = [ os.path.join(males_training_path, f) for f in os.listdir(males_training_path) ]
        files   = females + males
        return files

#------------------------------------------------------------------------------------------------------------------------------    
    
    # Function #3
    
    def identify_gender(self, vector):

        female_scores         = np.array(self.females_gmm.score(vector))
        female_log_likelihood = female_scores.sum()
        
        male_scores         = np.array(self.males_gmm.score(vector))
        male_log_likelihood = male_scores.sum()

        print("%10s %5s %1s" % ("+ Female Score",":", str(round(female_log_likelihood, 3))))
        print("%10s %7s %1s" % ("+ Male Score", ":", str(round(male_log_likelihood,3))))

        if male_log_likelihood > female_log_likelihood:
            winner = "male"
        else: 
            winner = "female"
        return winner

    
#---------------------------------------------------------------------------------------------------------------------------
    
    # Function #4
    
    def process(self):
        files = self.get_file_paths(self.females_training_path, self.males_training_path)

        for file in files:
            self.total_sample += 1
            print("%10s %8s %1s" % ("--> Testing", ":", os.path.basename(file)))

            vector = self.features_extractor.extract_features(file)
            winner = self.identify_gender(vector)
            expected_gender = file.split("/")[1][:-26]

            print("%10s %6s %1s" % ("+ Expectation",":", expected_gender))
            print("%10s %3s %1s" %  ("+ Identification", ":", winner))

            if winner != expected_gender:
                self.error += 1
            print("----------------------------------------------------")

        accuracy     = ( float(self.total_sample - self.error) / float(self.total_sample) ) * 100
        accuracy_msg = "*** Accuracy = " + str(round(accuracy, 3)) + "% ***"
        print(accuracy_msg)


#------------------------------------------------------------------------------------------------------------------------------

if __name__== "__main__":
    gender_identifier = Gender_Identifier("TestingData/females", "TestingData/males", "females.gmm", "males.gmm")
    gender_identifier.process()        
