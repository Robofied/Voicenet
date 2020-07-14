import pickle
import numpy as np
import os
import logging

from voicenet.utils import FeatureExtraction
from voicenet.utils import basic_utils


"""Setup"""
# logger setup
basic_utils.setup_logging()
logger = logging.getLogger(__name__)


## GLOBAL VARIABLES
MODELS = {'gmm': ['females_gmm_model.gmm', 'males_gmm_model.gmm']}
MODEL_DIR = 'models/'
# FEMALE_GMM_MODELFILE = 'females_gmm_model.gmm'
# MALE_GMM_MODELFILE = 'males_gmm_model.gmm'
class VoicePipeline():
    
    """ Final Pipeline for making prediction i.e, detecting gender from voice file
    
    Attributes
    ---------
    model: which model you want to use for prediction. List of available models = ['gmm']
    
    trained_models(Optional): Flag for using trained models dictionary.
    """
    
    def __init__(self, model="gmm", trained_models= None):
        
        if model not in MODELS:
            raise ValueError("{0} model is not supported. Please provide model from following list: {1}".format(model, MODELS.keys()))
            
        self.trained_models = MODELS[str(model)]
    
    def identify_gender(self, female_model, male_model, vector):
        
        """ Calculate score from gmm model for the vector
        
        Arguments:
            female_model: trained female gmm model
            male_model: trained male gmm model
            vector: mfcc feature vector for the voice file

        Returns:
            string: Male or Female based on score.
        """
    
        is_female_score = np.array(female_model.score(vector))
        is_female_log_likelihood = is_female_score.sum()
        
        is_male_score = np.array(male_model.score(vector))
        is_male_log_likelihood = is_male_score.sum()
        
        logger.info("Female Likelihood {0}".format(is_female_log_likelihood))
        logger.info("Male Likelihood {0}".format(is_male_log_likelihood))
            
        
        if is_male_log_likelihood > is_female_log_likelihood:
            winner = "Male" 
        else:
            winner = "Female"
        
        return winner   
    
    def predict(self, audiofile, trained_models=None):
        
        """ Converting voice file into mfcc feature and predict the gender
        
        Arguments:
            audiofile: audiofile for which we need to detect the gender

            trained_models(optional): Flag for using trained models dictionary.
        Returns:
            string: Female or Male based on score from identify_gender
        """
        
        mfccfeatures = FeatureExtraction.mfcc_feature(audiofile)
        
        logger.info("Getting trained models from directory")
        trained_models = self.trained_models
        print(trained_models)

        # file = 'data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav'

        female_model = pickle.load(open(os.path.join(MODEL_DIR, trained_models[0]),'rb'))
        male_model = pickle.load(open(os.path.join(MODEL_DIR, trained_models[1]), 'rb'))

        logger.info("Creating features for audofile")
        vector = mfccfeatures.get_features(audiofile)

        winner = self.identify_gender(female_model,male_model,vector)
        logging.info("Winner is {}".format(winner))
        
        return winner
        
 
if __name__ == "__main__":
    
    voicenet = VoicePipeline()  
    
    voicenet.predict('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')


# def identify_gender(female_model, male_model, vector):
    
#     winner = ''
    
#     is_female_score = np.array(female_model.score(vector))
#     is_female_log_likelihood = is_female_score.sum()
    
#     is_male_score = np.array(male_model.score(vector))
#     is_male_log_likelihood = is_male_score.sum()
    
#     print("Female Likelihood {0}".format(is_female_log_likelihood))
#     print("Male Likelihood {0}".format(is_male_log_likelihood))
        
    
#     if is_male_log_likelihood > is_female_log_likelihood:
#         winner = "Male" 
#     else:
#         winner = "Female"
    
#     return winner

# mfccfeatures = mfcc_features()

# file = 'data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav'

# female_model = pickle.load(open(os.path.join(MODEL_DIR, FEMALE_GMM_MODELFILE),'rb'))
# male_model = pickle.load(open(os.path.join(MODEL_DIR, MALE_GMM_MODELFILE), 'rb'))

# vector = mfccfeatures.get_features(file)

# winner = identify_gender(female_model,male_model,vector)
# print(winner)




    
        
    