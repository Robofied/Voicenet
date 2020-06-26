from sklearn.preprocessing import LabelEncoder
import os, pickle

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
    print("Moving!")
    print(group)
    for fname in group:
        print(src+ '/' + fname)
        os.rename(src + '/' + fname, dst + '/' + fname)
    
def save_gmm_model(gmm, name):
    
    filename = ''.join([name, '.gmm'])
    
    with open(filename, 'wb') as gmm_file:
        pickle.dump(gmm, gmm_file)
        
    
     
    