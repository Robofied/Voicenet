import os
import tarfile
import logging
import pathlib

# import download

import wget
from voicenet.training.data_preparation import SplitData


from pathlib import Path
import os, sys

# sys.path.insert(0, )

BASE_path = os.path.abspath(__file__)

print(BASE_path)

# print(os.path.abspath(sys.argv[0]))

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

print(pathlib.Path().absolute())


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
        # print("Files extraction was successful!")

    except:
        logging.info("No extraction was performed")
        # print("No extraction was performed !")

# @staticmethod


def stamerican(direc="../../../data/datasets"):
    """
    Download ST American English Speech data and extract the dataset using extract_dataset() function

    Arguments
    ----------
    direc: str
        Directory where the dataset will be stored
    """
    # print(os.getcwd())
    # cwd = os.path.dirname(__file__)
    # print(cwd)
    # cwd = pathlib.Path().absolute()
    # print(pathlib.Path().absolute())
    
    
    
    # cwd = os.path.dirname(os.path.abspath(__file__))
    # print(cwd)
    # # print(pwd)
    direc = os.path.normpath(os.path.join(BASE_path, direc))
    
    print(direc)
    

    if not os.path.exists(direc):
        os.makedirs(direc)
        
    if 'voicenet_venv/lib/python3.7/site-packages/Voicenet-0.1.0-py3.7.egg/' in direc:
        direc = direc.replace('voicenet_venv/lib/python3.7/site-packages/Voicenet-0.1.0-py3.7.egg/', '')
        
    print(direc)

    # Download SQuAD 1.1
    print("Downloading ST American English Corpus...")

    data_url = 'https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz'

    files = data_url.split("/")[-1]
    
    # print(os.path.join(direc, files))
    # print(os.path.normpath(os.path.join(direc, files)))
    if os.path.exists(os.path.join(direc, files)):
        print(files, "already downloaded")
        dataset_dir = os.path.join(direc, 'ST-AEDS')
        extract_dataset(files, dataset_dir)
        SplitData.staeds_data_preparation(dataset_dir)
        x_train, y_train = [os.path.join(dataset_dir, 'TrainingData/females/', voice_file) for voice_file in os.listdir(os.path.join(
            dataset_dir, 'TrainingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))))]
        x_train.extend([os.path.join(dataset_dir, 'TrainingData/males/', voice_file)
                        for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))])
        # x_train = [os.path.join(dataset_dir,'TrainingData/females/')+x for x in x_train]
        y_train.extend([1 for i in range(
            len(os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))))])

        x_test, y_test = [os.path.join(dataset_dir, 'TestingData/females/', voice_file) for voice_file in os.listdir(os.path.join(
            dataset_dir, 'TestingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/females'))))]
        x_test.extend([os.path.join(dataset_dir, 'TestingData/males/', voice_file)
                       for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/males'))])
        y_test.extend([1 for i in range(
            len(os.listdir(os.path.join(dataset_dir, 'TestingData/males'))))])

        return (x_train, y_train), (x_test, y_test)
    else:
        wget.download(url=data_url, out=direc)
        dataset_dir = os.path.join(direc, 'ST-AEDS')
        extract_dataset(files, dataset_dir)

        SplitData.staeds_data_preparation(dataset_dir)
        x_train, y_train = [os.path.join(dataset_dir, 'TrainingData/females/', voice_file) for voice_file in os.listdir(os.path.join(
            dataset_dir, 'TrainingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TrainingData/females'))))]
        x_train.extend([os.path.join(dataset_dir, 'TrainingData/males/', voice_file)
                        for voice_file in os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))])
        # x_train = [os.path.join(dataset_dir,'TrainingData/females/')+x for x in x_train]
        y_train.extend([1 for i in range(
            len(os.listdir(os.path.join(dataset_dir, 'TrainingData/males'))))])

        x_test, y_test = [os.path.join(dataset_dir, 'TestingData/females/', voice_file) for voice_file in os.listdir(os.path.join(
            dataset_dir, 'TestingData/females'))], [0 for i in range(len(os.listdir(os.path.join(dataset_dir, 'TestingData/females'))))]
        x_test.extend([os.path.join(dataset_dir, 'TestingData/males/', voice_file)
                       for voice_file in os.listdir(os.path.join(dataset_dir, 'TestingData/males'))])
        y_test.extend([1 for i in range(
            len(os.listdir(os.path.join(dataset_dir, 'TestingData/males'))))])

        return (x_train, y_train), (x_test, y_test)


# wget.download(url='https://github.com/Robofied/Voicenet/releases/download/v1.0/ST-AEDS-20180100_1-OS.tgz', out='.')
