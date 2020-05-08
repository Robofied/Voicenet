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
from utils import basic_utils, download
from features_extraction import mfcc_features


DATA_RAW_DIR = './data/raw'

download.download_extract_data()