# import voicenet.pipeline as vp

# voice = vp.cdqa_pipeline.VoicePipeline()

# from voicenet.models import GenderDetection
# from voicenet.training import GMMModelTraining

# voicenet = GenderDetection()  
    
# winner = voicenet.predict('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')

# print(winner)

# gmm_model = GMMModelTraining(staeds_flag=False)
# 
# gmm_model.train_model(data_dir='data/raw/test', data_dir_females='data/raw/test/females', data_dir_males='data/raw/test/males', model_dir='models/')

# from voicenet.training import Accuracy


# accuracy = Accuracy()

# accuracy.get_test_accuracy('data/raw/ST-AEDS/TestingData/females', 'data/raw/ST-AEDS/TestingData/males')

# from voicenet.training import SplitData
# from voicenet.training import SplitData

# SplitData.universal_data_preparation('data/raw/test', 'data/raw/test/females', 'data/raw/test/males')

# from voicenet.utils import FeatureExtraction

# from voicenet.utils import FeatureExtractn

# hg = FeatureExtraction.mfcc_feature(filename='data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')
# print(hg)
# FeatureExtraction.mfcc_feature()
from voicenet.datasets import stamerican

# stamerican()

(x_train, y_train), (x_test, y_test) = stamerican()

# print(x_train)

# print(y_test)

# from voicenet.feature_extraction import MFCC

# combined_features = MFCC('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')

# print(combined_features)


