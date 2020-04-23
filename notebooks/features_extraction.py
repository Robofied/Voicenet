from python_speech_features import mfcc
import scipy.io.wavfile as wav
import os


RAW_DATA_DIR = '../data/raw/ST-AEDS'

(rate,sig) = wav.read(os.path.join(RAW_DATA_DIR, "f0001_us_f0001_00001.wav"))
mfcc_feat = mfcc(sig,rate, lowfreq=0,)
print(mfcc_feat.shape)
print(mfcc_feat[:,8])