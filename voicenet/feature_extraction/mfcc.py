from python_speech_features import mfcc, delta
import scipy.io.wavfile as wav
from sklearn import preprocessing
import os
import numpy as np

# __all__ = ["FeatureExtraction", "mfcc_feature"]

# import _features_extraction

def MFCC(filename):
    
    (rate,sig) = wav.read(os.path.join(filename))
    mfcc_feature = mfcc(sig,rate, lowfreq=0,)
    mfcc_feature  = preprocessing.scale(mfcc_feature)
    deltas        = delta(mfcc_feature, 2)
    double_deltas = delta(deltas, 2)
    combined_feature      = np.hstack((mfcc_feature, deltas, double_deltas))
    
    return combined_feature

# class MFCC(object):
    
#     """ calculate mfcc features for voice file using python_speech_features
#     """
    
#     def __init__(self):
#         pass

#     # def __init__(self, RAW_DATA_DIR= '../data/raw/ST-AEDS'):
#     #     # self.filename = filename
#     #     self.RAW_DATA_DIR = RAW_DATA_DIR

#     @staticmethod
#     def get_feature(filename):
        
#         """ calculate numeric features(mfcc features) for voice file
        
#         Arguments:
#             filename: filename with path for which mfcc feature will be calculated

#         Returns:
#             np.array: array of shape 9*n(needs to be corrected) 
#         """

#         # (rate,sig) = wav.read(os.path.join(self.RAW_DATA_DIR, filename))
#         (rate,sig) = wav.read(os.path.join(filename))
#         mfcc_feature = mfcc(sig,rate, lowfreq=0,)
#         mfcc_feature  = preprocessing.scale(mfcc_feature)
#         deltas        = delta(mfcc_feature, 2)
#         double_deltas = delta(deltas, 2)
#         combined_feature      = np.hstack((mfcc_feature, deltas, double_deltas))

#         # print(combined_feature.shape)
#         # print(len(combined_feature))
#         return combined_feature

# if __name__ == "__main__":

#     mfcc_features = mfcc_features()
#     mfcc_features.get_features('f0001_us_f0001_00001.wav')