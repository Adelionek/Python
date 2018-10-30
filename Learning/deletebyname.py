import os

os.chdir('C:\\test')
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        print(filename)
