import os

def verify_file_exists(file):
    #print("Current directory is: '{}' ".format(os.path.abspath(os.curdir)))
    #print("Verifying if a file '{}' exists: ".format(file))
    current_dir = os.path.abspath(os.curdir)
    if os.path.isfile(current_dir + file):
        #print("Verified: File '{}' exists".format(file))
        return True
    else:
        print("ERROR: File '{}' does not exist".format(file))
        return False

def verify_folder_exists(folder):
    if os.path.isdir(folder):
        print("Verified: Folder '{}' exists".format(folder))
        return True
    else:
        print("ERROR: Folder '{}' does not exist".format(folder))
        return False

def get_file_line_count(file):
        f = open(file)
        data = f.readlines()
        f.close()
        return len(data)