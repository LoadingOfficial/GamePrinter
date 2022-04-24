import os
import glob

def latest(directory):
    try:
        files = glob.glob(directory + "/*")
        latest_file = max(files, key=os.path.getctime).replace("\\","/")
        return latest_file
    except:
        print("Directory not found")
        exit()

def number(directory):
    file_count = 0
    try:
        for path in os.listdir(directory):
            file_count += 1
        return file_count
    except:
        print("Directory not found")
        exit()