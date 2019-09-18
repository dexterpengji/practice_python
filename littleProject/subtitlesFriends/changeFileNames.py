import os
# Use mac/ubuntu to run this script

path = 'source/'

# get the list of file names
fileList = os.listdir(path)

# change names
for i, x in enumerate(fileList):
    # old file name with path
    name_old = path + os.sep + x

    # new file name, and add path
    filename_new = x.split(".")[1] + ".ass"
    name_new = path + os.sep + filename_new

    # change names
    os.rename(name_old, name_new)
    print(name_old, ' ===> ', name_new)
