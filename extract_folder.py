import os
import shutil
import app as AppMain

def extractFolders(folders):
    try:
        for folder_single in folders:
            temp_files = os.listdir(folder_single)
            print(f'Extraindo da pasta {folder_single}')
            for i in temp_files:
                tempDir = os.path.join(folder_single,i)
                try:
                    if os.path.isdir(tempDir):
                        for j in os.listdir(tempDir):
                            shutil.move(os.path.join(tempDir,j),folder_single)
                        
                except OSError as e:
                    print(e)
            
    except OSError as e:
        print(e)

