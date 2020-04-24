from python_speech_features import mfcc
import scipy.io.wavfile as wav
import os


class mfcc_features(object):

    def __init__(self, filename, RAW_DATA_DIR= '../data/raw/ST-AEDS'):
        self.filename = filename
        self.RAW_DATA_DIR = RAW_DATA_DIR

    def get_features(self):

        print(self.RAW_DATA_DIR)
        print(self.filename)
        (rate,sig) = wav.read(os.path.join(self.RAW_DATA_DIR, self.filename))
        mfcc_feat = mfcc(sig,rate, lowfreq=0,)
        print(mfcc_feat.shape)
        print(mfcc_feat[:,8])

        return mfcc_feat

if __name__ == "__main__":

    mfcc_features = mfcc_features('f0001_us_f0001_00001.wav')
    mfcc_features.get_features()