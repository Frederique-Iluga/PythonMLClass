import pandas as pd
import numpy as np
import os
import os.path
import glob

def read_dataset(path):
    '''
    the function reads the dataset via a path and returns a dataframe
    
    '''
    df=pd.read_csv(path)
    return df

def is_file_exist(path):
    '''
    The function checks the full path's existence in the current directory and returns a boolean
    '''
    full_path = os.path.join(os.getcwd(), path)
    return os.path.isfile(full_path)

def check_file(filename):
    '''
    If the file in path exists return true, else false
    
    '''
    fullname = os.path.join(os.getcwd(), filename)
    
    if os.path.isfile(fullname):
        return True
    else:
        return False
    
#We create this function to be reusable
    
def read_dataset(path, col_names = None):
    '''
    The function reads the dataset via a path and returns a dataframe
    '''
    if check_file(path) == True:
        df=pd.read_csv(path, header = col_names)
    else:
        df = None
    return df


def list_file_with_extension(extension):
    '''
    This function returns the list of the files with a given etension in the current directory
    '''
    current_directory = os.getcwd()
    all_files = list_files_cur()
    result = [file for file in all_files if file.endswith(extension)]
    return result


def clean_extension(extension):
    '''
    This function cleans the extension given as parameter : removes the spaces and/or dot
    '''
    clean_extension = extension.strip()
    if clean_extension.startswith('.'): # Check if there is a . at the begining of the extension
        clean_extension = clean_extension[1:] # if yes, select only the extension fomr the 2nd character
    return clean_extension

def list_file_with_extension_cur_glob(extension):
    '''
    This function returns the list of the files with a given extension in the current directory
    using glob
    '''
    extension = clean_extension(extension)
    allowed = ['pdf','csv','data','txt'] # list of allowed extensions
    try:
        if extension not in allowed:
            raise ValueError
        else:
            current_directory = os.getcwd()
            full_path = os.path.join(current_directory, '*.' + extension)
            return glob.glob(f"*.{extension}")
    except:
        print('Extension used is not allowed, please used one of these : ')
        print(str(allowed))
