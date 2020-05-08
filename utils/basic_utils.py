from sklearn.preprocessing import LabelEncoder
import os

def label_encoder(list_cat_var):
    le = LabelEncoder()
    le.fit(list_cat_var)
    list_cat_var = le.transform(list_cat_var)
    return list_cat_var

def make_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(folder_path, "is created !")
    except:
        print("Exception raised: ", folder_path, "could not be created !")
        
def move_files(src, dst, group):
    for fname in group:
        os.rename(src + '/' + fname, dst + '/' + fname)
    