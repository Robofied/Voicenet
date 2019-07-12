import numpy as np
import pandas as pd
from scipy.io import wavfile
from os import path
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

# class build_features:
    
#     def take_audio(self, parameter_list):
#         print("inside take_audio")
#         samplerate, audio_data = wavfile.read('../data/internal/audio.wav')
#         print(samplerate)
        # check the format of the audio
        # supported are: mp3, 3gp and wav
        # if not then raise error to give supported audio
        # if format is correct then proceed further
        # take audio input and extract raw features from it and store it in a data structure

    # def process_audio(self, parameter_list):
    #     print("inside process_audio")
        # take list of raw features and start with feature engineering 
        # engineer all 20 features and save it in a list
        # return list of final features as a output
    

samplerate, audio_data = wavfile.read("audio1.wav")
# plt.plot(audio_data[:200])
freqs = fftfreq(audio_data.shape[0],1/samplerate)
spec = np.abs(np.fft.rfft(audio_data))
amp = spec[:,0] / spec[:,0].sum()
mean = (freqs * amp).sum()

z = amp - amp.mean() 
w = amp.std() 

sd = np.sqrt(np.sum(amp * ((freqs - mean) ** 2)))
amp_cumsum = np.cumsum(amp)
median = freqs[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
mode = freqs[amp.argmax()]
Q25 = freqs[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
Q75 = freqs[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
IQR = Q75 - Q25
skew = ((z ** 3).sum() / (len(spec[:,0]) - 1)) / w ** 3
kurt = ((z ** 4).sum() / (len(spec[:,0]) - 1)) / w ** 4
meanfreq = np.mean(freqs)
meanfun = np.average(freqs)
minfun = np.min(freqs)
maxfun = np.max(freqs)


#list_schema = ['kurt', 'sp.ent', 'sfm', 'mode', 'centroid', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindx', 'label']
feature_set = [meanfreq, sd, median, Q25, Q75, IQR,  skew, kurt, mode, meanfun, minfun, maxfun]
print("Feature List: ", feature_set)