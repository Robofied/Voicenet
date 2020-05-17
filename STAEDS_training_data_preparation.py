import math
import os


def get_fnames_from_dict(self, dataset_dict, f_or_m):
        training_data, testing_data = [], []

        for i in range(1,5):
            length_data       = len(dataset_dict[f_or_m +"000" + str(i)])
            length_separator  = math.trunc(length_data*2/3)

            training_data += dataset_dict[f_or_m + "000" + str(i)][:length_separator]
            testing_data  += dataset_dict[f_or_m + "000" + str(i)][length_separator:]

        return training_data, testing_data
    
def manage(dataset_directory):
    
        # compressed_dataset_file_name = dataset_path
        # dataset_directory = compressed_dataset_file_name.split(".")[0]

        # try:
        #     os.mkdir(dataset_directory)
        # except:
        #     pass

        # self.extract_dataset(compressed_dataset_file_name, dataset_directory)

        file_names   = [fname for fname in os.listdir(dataset_directory) if ("f0" in fname or "m0" in fname)]
        dataset_dict = {"f0001": [], "f0002": [], "f0003": [], "f0004": [], "f0005": [],
                        "m0001": [], "m0002": [], "m0003": [], "m0004": [], "m0005": [], }

        for fname in file_names:
            dataset_dict[fname.split('_')[0]].append(fname)

        training_set, testing_set = {},{}
        training_set["females"], testing_set["females"] = get_fnames_from_dict(dataset_dict, "f")
        training_set["males"  ], testing_set["males"  ] = get_fnames_from_dict(dataset_dict, "m")

        self.make_folder("TrainingData")
        self.make_folder("TestingData")
        self.make_folder("TrainingData/females")
        self.make_folder("TrainingData/males")
        self.make_folder("TestingData/females")
        self.make_folder("TestingData/males")

        self.move_files(dataset_directory, "TrainingData/females", training_set["females"])
        self.move_files(dataset_directory, "TrainingData/males",   training_set["males"])
        self.move_files(dataset_directory, "TestingData/females",  testing_set["females"])
        self.move_files(dataset_directory, "TestingData/males",    testing_set["males"])