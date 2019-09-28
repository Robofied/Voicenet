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

class Data_Manager:
    # Function #1
    
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

#-------------------------------------------------------------------------------------------------------------------------------
    # Function #2
    
    def extract_dataset(self, compressed_dataset_file_name, dataset_directory):
        try:
            tar = tarfile.open(compressed_dataset_file_name, "r:gz")
            tar.extractall(dataset_directory)
            tar.close()
            print("Files extraction was successful!")

        except:
            print("No extraction was performed !")
            
#-------------------------------------------------------------------------------------------------------------------------------
    # Function #3
    
    def make_folder(self, folder_path):
        try:
            os.mkdir(folder_path)
            print(folder_path, "was created !")
        except:
            print("Exception raised: ", folder_path, "could not be created !")
            
#-------------------------------------------------------------------------------------------------------------------------------
    # Function #4
    
    def get_fnames_from_dict(self, dataset_dict, f_or_m):
        training_data, testing_data = [], []

        for i in range(1,5):
            length_data       = len(dataset_dict[f_or_m +"000" + str(i)])
            length_separator  = math.trunc(length_data*2/3)

            training_data += dataset_dict[f_or_m + "000" + str(i)][:length_separator]
            testing_data  += dataset_dict[f_or_m + "000" + str(i)][length_separator:]

        return training_data, testing_data
    
#------------------------------------------------------------------------------------------------------------------------------   
    # Function #5
    
    def move_files(self, src, dst, group):
        for fname in group:
            os.rename(src + '/' + fname, dst + '/' + fname)

#------------------------------------------------------------------------------------------------------------------------------
    # Function #6
    
    def manage(self):

        compressed_dataset_file_name = self.dataset_path
        dataset_directory = compressed_dataset_file_name.split(".")[0]

        try:
            os.mkdir(dataset_directory)
        except:
            pass

        self.extract_dataset(compressed_dataset_file_name, dataset_directory)

        file_names   = [fname for fname in os.listdir(dataset_directory) if ("f0" in fname or "m0" in fname)]
        dataset_dict = {"f0001": [], "f0002": [], "f0003": [], "f0004": [], "f0005": [],
                        "m0001": [], "m0002": [], "m0003": [], "m0004": [], "m0005": [], }

        for fname in file_names:
            dataset_dict[fname.split('_')[0]].append(fname)

        training_set, testing_set = {},{}
        training_set["females"], testing_set["females"] = self.get_fnames_from_dict(dataset_dict, "f")
        training_set["males"  ], testing_set["males"  ] = self.get_fnames_from_dict(dataset_dict, "m")

        self.make_folder("TrainingData")
        self.make_folder("TestingData")
        self.make_folder("TrainingData/females")
        self.make_folder("TrainingData/males")
        self.make_folder("TestingData/females")
        self.make_folder("TestingData/males")

        self.move_files(dataset_directory, "TrainingData/females", training_set["females"])
        self.move_files(dataset_directory, "TrainingData/males",   training_set["males"])
        self.move_files(dataset_directory, "TestingData/females",  testing_set["females"])
        self.move_files(dataset_directory, "TestingData/males",    testing_set["males"])

#-------------------------------------------------------------------------------------------------------------------------------

if __name__== "__main__":
    data_manager = Data_Manager("SLR45.tgz")
    data_manager.manage()