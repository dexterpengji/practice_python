import os
path_source = 'source/'

# get the list of file names
fileList = os.listdir(path_source)
fileList.sort()
print(fileList)

# get the words from all files
"""
for i, x in enumerate(fileList):
    with open(path_source + os.sep + x, mode="r") as file:
        content_fulltext = file.read()
        print(content_fulltext)
    print(x)
    break

"""
