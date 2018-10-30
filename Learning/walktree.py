import os

for folderName, subfolders, filenamesx in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenamesx:
        print('File inside '+folderName+': '+filename)
