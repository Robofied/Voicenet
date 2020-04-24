from python_speech_features import mfcc, delta
import scipy.io.wavfile as wav
from sklearn import preprocessing
import os
import numpy as np

class mfcc_features(object):

    def __init__(self, filename, RAW_DATA_DIR= '../data/raw/ST-AEDS'):
        self.filename = filename
        self.RAW_DATA_DIR = RAW_DATA_DIR

    def get_features(self):

        (rate,sig) = wav.read(os.path.join(self.RAW_DATA_DIR, self.filename))
        mfcc_feature = mfcc(sig,rate, lowfreq=0,)
        mfcc_feature  = preprocessing.scale(mfcc_feature)
        deltas        = delta(mfcc_feature, 2)
        double_deltas = delta(deltas, 2)
        combined_feature      = np.hstack((mfcc_feature, deltas, double_deltas))

        return combined_feature

if __name__ == "__main__":

    mfcc_features = mfcc_features('f0001_us_f0001_00001.wav')
    mfcc_features.get_features()