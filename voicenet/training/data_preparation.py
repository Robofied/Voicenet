import math
import os
from voicenet.utils.basic_utils import make_folder, move_files


class SplitData:
    
    def __init__(self):
        pass

    @staticmethod
    def get_fnames_from_dict(dataset_dict, f_or_m):
        training_data, testing_data = [], []

        for i in range(1,6):
            length_data       = len(dataset_dict[str(f_or_m +"000" + str(i))])
            length_separator  = math.trunc(length_data*2/3)
            
            print(f_or_m +"000" + str(i))
            print(length_data)
            print(length_separator)
            print(dataset_dict)
            print(dataset_dict[f_or_m + "000" + str(i)][:length_separator])
            

            training_data.extend(dataset_dict[f_or_m + "000" + str(i)][:length_separator])
            testing_data.extend(dataset_dict[f_or_m + "000" + str(i)][length_separator:])
            # print(training_data)
            

        # print("Training data:", training_data)
        return training_data, testing_data
     
    @staticmethod   
    def staeds_data_preparation(dataset_directory):
        
        # compressed_dataset_file_name = dataset_path
        # dataset_directory = compressed_dataset_file_name.split(".")[0]

        # try:
        #     os.mkdir(dataset_directory)
        # except:
        #     pass

        # self.extract_dataset(compressed_dataset_file_name, dataset_directory)

        file_names   = [fname for fname in os.listdir(dataset_directory) if ("f0" in fname or "m0" in fname)]
        # print(file_names)
        dataset_dict = {"f0001": [], "f0002": [], "f0003": [], "f0004": [], "f0005": [],
                        "m0001": [], "m0002": [], "m0003": [], "m0004": [], "m0005": [], }

        for fname in file_names:
            dataset_dict[fname.split('_')[0]].append(fname)
            
        # print(dataset_dict)
        training_set, testing_set = {},{}
        training_set["females"], testing_set["females"] = SplitData.get_fnames_from_dict(dataset_dict, "f")
        training_set["males"  ], testing_set["males"  ] = SplitData.get_fnames_from_dict(dataset_dict, "m")
        print(training_set["females"])

        make_folder(os.path.join(dataset_directory, "TrainingData"))
        make_folder(os.path.join(dataset_directory, "TestingData"))
        make_folder(os.path.join(dataset_directory, "TrainingData/females"))
        make_folder(os.path.join(dataset_directory, "TrainingData/males"))
        make_folder(os.path.join(dataset_directory, "TestingData/females"))
        make_folder(os.path.join(dataset_directory, "TestingData/males"))

        move_files(dataset_directory, os.path.join(dataset_directory, "TrainingData/females"), training_set["females"])
        move_files(dataset_directory, os.path.join(dataset_directory, "TrainingData/males"),   training_set["males"])
        move_files(dataset_directory, os.path.join(dataset_directory, "TestingData/females"),  testing_set["females"])
        move_files(dataset_directory, os.path.join(dataset_directory, "TestingData/males"),    testing_set["males"])
            
    @staticmethod
    def universal_data_preparation(dataset_directory, females_directory, males_directory):
        
        training_set = {}
        testing_set = {}
        
        make_folder(os.path.join(dataset_directory, "TrainingData"))
        make_folder(os.path.join(dataset_directory, "TestingData"))
        make_folder(os.path.join(dataset_directory, "TrainingData/females"))
        make_folder(os.path.join(dataset_directory, "TrainingData/males"))
        make_folder(os.path.join(dataset_directory, "TestingData/females"))
        make_folder(os.path.join(dataset_directory, "TestingData/males"))
        
        file_name_females = [fname for fname in os.listdir(females_directory)]
        file_name_males = [fname for fname in os.listdir(males_directory)]
        
        female_length_separator  = math.trunc(len(file_name_females)*2/3)
        male_length_separator = math.trunc(len(file_name_males)*2/3)
        
        training_set["females"] = file_name_females[:female_length_separator]
        training_set["males"] = file_name_males[:male_length_separator]
        testing_set["females"] = file_name_females[female_length_separator:]
        testing_set["males"] = file_name_males[male_length_separator:]
        
        move_files(os.path.join(dataset_directory, "females"), os.path.join(dataset_directory, "TrainingData/females"), training_set["females"])
        move_files(os.path.join(dataset_directory, "males"), os.path.join(dataset_directory, "TrainingData/males"),   training_set["males"])
        move_files(os.path.join(dataset_directory, "females"), os.path.join(dataset_directory, "TestingData/females"),  testing_set["females"])
        move_files(os.path.join(dataset_directory, "males"), os.path.join(dataset_directory, "TestingData/males"),    testing_set["males"])
        
        
        
        
        
        
        
        
        
        
        