import os
from glob import *

def latest_files(directory, ammount):
    latest_files = glob(directory + "\\" + "*.*")
    latest_files.sort(reverse = True, key = os.path.getctime)
    latest_files = [files.replace("\\","/") for files in latest_files]

    return latest_files[:int(ammount)]

def number_of_files(directory):
    file_count = 0
    try:
        for path in os.listdir(directory):
            file_count  += 1
        return file_count
    except:
        print("Directory not found")
        exit()