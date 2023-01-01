import os
import app as AppMain

def deleteFolders(folders):
    try:
        for folder_single in folders:
            temp_files = os.listdir(folder_single)
            print(f'Deletando pastas vazias da pasta {folder_single}')
            for i in temp_files:
                tempDir = os.path.join(folder_single,i)
                try:
                    if os.path.isdir(tempDir) and len(os.listdir(tempDir)) == 0:
                        os.removedirs(tempDir)
                        
                except OSError as e:
                    print(e)
            
    except OSError as e:
        print(e)

if __name__ == '__main__':
    deleteFolders(AppMain.returnFolders())
