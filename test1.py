# import voicenet.pipeline as vp

# voice = vp.cdqa_pipeline.VoicePipeline()

from voicenet.pipeline import VoicePipeline

voicenet = VoicePipeline()  
    
winner = voicenet.predict('data/raw/ST-AEDS/TestingData/females/f0001_us_f0001_00005.wav')

print(winner)