import os

from voicenet.pipeline import VoicePipeline


class Accuracy:
    
    def __init__(self, error=None):
        
        self.error = 0
    
    @staticmethod
    def get_files_list(females_dir, males_dir):
        
        females_filepath_gender = [(os.path.join(females_dir, f), 'female') for f in os.listdir(females_dir) ]
        males_filepath_gender   = [(os.path.join(males_dir, f), 'male') for f in os.listdir(males_dir) ]
        files   = females_filepath_gender + males_filepath_gender
        return files

    def get_test_accuracy(self, data_dir_females, data_dir_males):
        
        files = Accuracy.get_files_list(data_dir_females, data_dir_males)
        voicenet = VoicePipeline()
        
        for f in files:
            
            predicted_winner = voicenet.predict(f[0])
            expected_winner = f[1]
            
            if predicted_winner == expected_winner:
                self.error += 1
                
        acc = ((len(f) - self.error)/len(f)) * 100  
        print("Testing Accuracy {0}%".format(acc))
        
            
            
            
        
        
        
        