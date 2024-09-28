import os
import glob

def delete_files(path):
    file_list = glob.glob(path + '/*')
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f'{file_path} has been deleted.')
        except Exception as e:
            print(f'Error occurred while deleting {file_path}. Error message: {e}')
path = input("Please input the path of the folder to clear.")
delete_files(path)