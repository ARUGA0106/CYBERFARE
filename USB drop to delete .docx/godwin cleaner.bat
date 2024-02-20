@py.exe "C:\Users\PC\Desktop\USB\PythonScript.py" %*
import os
import glob

path_folder = r'C:\Users\Sirkal\Desktop\2DO' # the directory of the files to be deleted
file_extension = '.dox' #the extension file to be deleted

for file in glob.glob(path_folder + '/*' + file_extension):
    os.copy(file)