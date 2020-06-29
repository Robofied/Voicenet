import pickle
import numpy as np
import os

from utils.features_extraction import mfcc_features

MODEL_DIR = 'models/'
FEMALE_GMM_MODELFILE = 'females_gmm_model.gmm'
MALE_GMM_MODELFILE = 'males_gmm_model.gmm'


def identify_gender(female_model, male_model, vector):
    
    winner = ''
    
    is_female_score = np.array(female_model.score(vector))
    is_female_log_likelihood = is_female_score.sum()
    
    is_male_score = np.array(male_model.score(vector))
    is_male_log_likelihood = is_male_score.sum()
    
    print("Female Likelihood {0}".format(is_female_log_likelihood))
    print("Male Likelihood {0}".format(is_male_log_likelihood))
        
    
    if is_male_log_likelihood > is_female_log_likelihood:
        winner = "Male" 
    else:
        winner = "Female"
    
    return winner

mfccfeatures = mfcc_features()

file = 'data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav'

female_model = pickle.load(open(os.path.join(MODEL_DIR, FEMALE_GMM_MODELFILE),'rb'))
male_model = pickle.load(open(os.path.join(MODEL_DIR, MALE_GMM_MODELFILE), 'rb'))

vector = mfccfeatures.get_features(file)

winner = identify_gender(female_model,male_model,vector)
print(winner)




    
        
    