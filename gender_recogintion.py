import pickle
import numpy as np

def identify_gender(female_model, male_model, vector):
    
    is_female_score = np.array(female_model.score(vector))
    is_female_log_likelihood = is_female_score.sum()
    
    is_male_score = np.array(male_model.score(vector))
    is_male_log_likelihood = is_male_score.sum()
    
    print("Female Likelihood {0}".format(is_female_log_likelihood))
    print("Male Likelihood {0}".format()(is_male_log_likelihood))
    
    winner = 'Male' if is_male_log_likelihood > is_female_log_likelihood else 'Female'
    
    return winner


    
        
    