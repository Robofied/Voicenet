import os

from voicenet.pipeline import VoicePipeline


class Accuracy:
    
    """ getting the accuracy of trained model
    
    Attributes
    ---------
    error: int
    initiliazed with 0
    
    
    Methods
    -------
    
    get_files_list(females_dir, males_dir): returns the list of all files in females and males directory
    
    get_test_accuracy(self, data_dir_females, data_dir_males): calculate the accuracy over testing data
        
        
        
    """
    
    def __init__(self, error=None):
        
        self.error = 0
    
    @staticmethod
    def get_files_list(females_dir: str, males_dir: str) -> list:
        
        """ combine the list of all files in females and males directory
        
        Arguments:
            [females_dir]: [directory which contains females voice]
            [males_dir]: [directory which contaisn males voice]
            

        Returns:
            [files]: [list of files]
        """
        
        females_filepath_gender = [(os.path.join(females_dir, f), 'female') for f in os.listdir(females_dir) ]
        males_filepath_gender   = [(os.path.join(males_dir, f), 'male') for f in os.listdir(males_dir) ]
        files   = females_filepath_gender + males_filepath_gender
        return files

    def get_test_accuracy(self, data_dir_females: str, data_dir_males: str):
        
        """ calculate the test accuracy
        
        Arguments:
            data_dir_females: [directory contains testing females voices]
            
            data_dir_males: [directory contains testing males voices]
        
        """
        
        files = Accuracy.get_files_list(data_dir_females, data_dir_males)
        voicenet = VoicePipeline()
        
        for f in files:
            
            predicted_winner = voicenet.predict(f[0])
            expected_winner = f[1]
            
            if predicted_winner == expected_winner:
                self.error += 1
                
        acc = ((len(f) - self.error)/len(f)) * 100  
        print("Testing Accuracy {0}%".format(acc))
        
            
            
            
        
        
        
        