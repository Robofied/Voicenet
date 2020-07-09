from sklearn.preprocessing import LabelEncoder
import os, pickle
import logging
import logging.config
import yaml


def setup_logging(
    default_path:str = '../logConfig.yaml', 
    default_level:int = logging.INFO,
    env_key:str = 'LOG_CFC'
):
    """
    Setup logging configuration
    """
    
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as file:
            config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def label_encoder(list_cat_var: list) -> list:
    
    """ returning the encoded labels using label encoder
    
    Arguments:
        list_car_var: list of categories

    Returns:
        list: encoded values for a input list
    """
    le = LabelEncoder()
    le.fit(list_cat_var)
    list_cat_var = le.transform(list_cat_var)
    return list_cat_var

def make_folder(folder_path):
    
    """ create an empty folder in specified folder path
    
    Arguments:
        folder_path: path for folder to be created  
    
    """
    try:
        os.mkdir(folder_path)
        print(folder_path, "is created !")
    except:
        print("Exception raised: ", folder_path, "could not be created !")
        
def move_files(src, dst, group):
    
    """ Move file from source to destination
    
    Arguments:
        src: file to move from
        
        dst: file to be moved to destination
        
        group: list of file names to be move
    """
    print("Moving!")
    print(group)
    for fname in group:
        print(src+ '/' + fname)
        os.rename(src + '/' + fname, dst + '/' + fname)
    
def get_file_paths(females_training_path: str, males_training_path: str) -> list:
    
    """ getting list of path of female and male directory
    
    Arguments:
        females_training_path: female_folder_path
        
        males_training_path: male_folder_path

    Returns:
        list: list of females, males voice files with thier paths 
    """
    
    females = [ os.path.join(females_training_path, f) for f in os.listdir(females_training_path) ]
    males = [ os.path.join(males_training_path, f) for f in os.listdir(males_training_path) ]
    
    return females, males

def save_gmm_model(gmm, directory_file_name):
    
    """ saving the trained model
    
    Arguments:
        gmm: gmm model trained
        
        directory_file_name: directory where gmm model will be saved
    """
    
    logging.info("Saving gmm model")
    
    filename = ''.join([directory_file_name, '.gmm'])
    
    with open(filename, 'wb') as gmm_file:
        pickle.dump(gmm, gmm_file)
        
    
     
    