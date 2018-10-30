#! Program that compress folder to .zip file

import zipfile, os


def backupToZip(path):

    folder = os.path.abspath(path)
    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #   TODO: create the zip file

    print('Creating %s...' % (zipFilename))

    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk down, compress each file in each folder

    for foldername, subfolders, filenames in os.walk(folder):

        print('Adding files in %s...' % foldername)
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'

            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

backupToZip(input("Type the folder path:"))
print(input("Press any key to exit"))