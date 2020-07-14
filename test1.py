# import voicenet.pipeline as vp

# voice = vp.cdqa_pipeline.VoicePipeline()

# from voicenet.pipeline import VoicePipeline
# from voicenet.training import GMMModelTraining

# voicenet = VoicePipeline()  
    
# winner = voicenet.predict('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')

# print(winner)

# gmm_model = GMMModelTraining(staeds_flag=False)

# gmm_model.train_model(data_dir='data/raw/test', data_dir_females='data/raw/test/females', data_dir_males='data/raw/test/males', model_dir='models/')

# from voicenet.training import Accuracy


# accuracy = Accuracy()

# accuracy.get_test_accuracy('data/raw/ST-AEDS/TestingData/females', 'data/raw/ST-AEDS/TestingData/males')

# from voicenet.training import SplitData
# from voicenet.training import SplitData

# SplitData.universal_data_preparation('data/raw/test', 'data/raw/test/females', 'data/raw/test/males')

from voicenet.utils import FeatureExtraction

# from voicenet.utils import FeatureExtractn

hg = FeatureExtraction.mfcc_feature(filename='data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')
print(hg)
# FeatureExtraction.mfcc_feature()



