import extract_folder as EF
import os


def returnFolders():
    folders = [os.getcwd().replace('\\','/')]
    return folders

if __name__ == '__main__':
    EF.extractFolders(returnFolders())