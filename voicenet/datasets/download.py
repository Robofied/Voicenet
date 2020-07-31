import os
import wget
import tarfile
from voicenet.training.data_preparation import SplitData
    
    
def extract_dataset(compressed_dataset_file_name: str, dataset_directory: str):
    
    """ extract dataset from compressed file
    
    Arguments:
        compressed_dataset_file_name: compresses dataset filename
        
        dataset_directory: directory path where dataset to be extracted
    """
    
    try:
        tar = tarfile.open(compressed_dataset_file_name, "r:gz")
        tar.extractall(dataset_directory)
        tar.close()
        print("Files extraction was successful!")

    except:
        print("No extraction was performed !")

# @staticmethod
def stamerican(direc= "."):
    """
    Download ST American English Speech data and extract the dataset using extract_dataset() function

    Arguments
    ----------
    direc: str
        Directory where the dataset will be stored
    """

    direct = os.path.expanduser(direc)
    print(direct)

    if not os.path.exists(direc):
        os.makedirs(direc)

    # Download SQuAD 1.1
    print("Downloading ST American English Corpus...")

    data_url = 'https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz'
    
    file = data_url.split("/")[-1]
    if os.path.exists(os.path.join(direc, file)):
        print(file, "already downloaded")
        dataset_dir = os.path.join(direc, 'ST-AEDS')
        extract_dataset(file, dataset_dir)
        SplitData.staeds_data_preparation(dataset_dir)
        x_train, y_train = [os.path.join(dataset_dir,'TrainingData/females/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))))]
        x_train.extend([os.path.join(dataset_dir,'TrainingData/males/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))])
        # x_train = [os.path.join(dataset_dir,'TrainingData/females/')+x for x in x_train]
        y_train.extend([1 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))))])
        
        x_test, y_test = [os.path.join(dataset_dir,'TestingData/females/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/females'))))]
        x_test.extend([os.path.join(dataset_dir,'TestingData/males/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/males'))])
        y_test.extend([1 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/males'))))])
        
        return (x_train, y_train), (x_test, y_test)
    else:
        wget.download(url=data_url, out=direc)
        dataset_dir = os.path.join(direc, 'ST-AEDS')
        extract_dataset(file, dataset_dir)
        
        SplitData.staeds_data_preparation(dataset_dir)
        x_train, y_train = [os.path.join(dataset_dir,'TrainingData/females/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))))]
        x_train.extend([os.path.join(dataset_dir,'TrainingData/males/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))])
        # x_train = [os.path.join(dataset_dir,'TrainingData/females/')+x for x in x_train]
        y_train.extend([1 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))))])
        
        x_test, y_test = [os.path.join(dataset_dir,'TestingData/females/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/females'))))]
        x_test.extend([os.path.join(dataset_dir,'TestingData/males/',voice_file) for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/males'))])
        y_test.extend([1 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/males'))))])
 
        return (x_train, y_train), (x_test, y_test)
        




# wget.download(url='https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz', out='.')

    