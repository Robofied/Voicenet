from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav


def GetMfcc(filename):
    (rate,sig) = wav.read(filename)
    mfcc_feat = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)
    return mfcc_feat