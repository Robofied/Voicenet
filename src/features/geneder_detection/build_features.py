import numpy as np
import pandas as pd
from scipy.io import wavfile

class build_features:
    
    def take_audio(self, parameter_list):
        print("inside take_audio")
        samplerate, audio_data = wavfile.read('../data/internal/file_example_WAV_1MG.wav')
        # check the format of the audio
        # supported are: mp3, 3gp and wav
        # if not then raise error to give supported audio
        # if format is correct then proceed further
        # take audio input and extract raw features from it and store it in a data structure

    def process_audio(self, parameter_list):
        print("inside process_audio")
        # take list of raw features and start with feature engineering 
        # engineer all 20 features and save it in a list
        # return list of final features as a output
    
    