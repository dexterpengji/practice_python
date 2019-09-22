import os
import cv2

path = '/Users/pengji/Desktop/brainstormPicture'

# get the list of file names
fileList = os.listdir(path)
num_files = len(fileList)
print("working path: %s" % path)
print("number of files: %s" % num_files)
input("press enter to continue, or press CTRL+C to quit.")

# change names
for i, x in enumerate(fileList):
    if x[-4:].lower() == ".jpg" and x[:9] != "_cropped_":
        # old file name with path
        name_old = path + os.sep + x

        # new file name, and add path
        filename_new = "_cropped_" + x
        name_new = path + os.sep + filename_new

        # read the picture
        img = cv2.imread(name_old)
        img = img[130:1710, 1250:3180]
        cv2.imwrite(name_new, img)
        print(x, ' ===> cropped')
    else:
        print("not a valid file: %s " % x)