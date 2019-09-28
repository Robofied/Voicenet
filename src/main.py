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

#import libraries
import Features_Extractor
import Data_Manager
import Model_Trainer
import Gender_Identifier