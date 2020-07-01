# import voicenet.pipeline as vp

# voice = vp.cdqa_pipeline.VoicePipeline()

# from voicenet.pipeline import VoicePipeline
# from voicenet.training import GMMModelTraining

# voicenet = VoicePipeline()  
    
# winner = voicenet.predict('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')

# print(winner)

# gmm_model = GMMModelTraining()

# gmm_model.train_model('data/raw', 'models/')

from voicenet.training import Accuracy


accuracy = Accuracy()

accuracy.get_test_accuracy('data/raw/ST-AEDS/TestingData/females', 'data/raw/ST-AEDS/TestingData/males')




