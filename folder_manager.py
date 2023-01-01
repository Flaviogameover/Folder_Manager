import app as AppMain
import extract_folder as EF
import delete_empty as DE


# print current folder

EF.extractFolders(AppMain.returnFolders())
DE.deleteFolders(AppMain.returnFolders())