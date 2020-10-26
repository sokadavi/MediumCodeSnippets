import os
import cv2

# the 'r' before the string deactivates the backslash-breaking
root_folder = r"C:\your_folder_structure\semantic_matting_dataset"


for subdir, dirs, files in os.walk(root_folder):
    for filename in files:
        filepath = subdir + os.sep + filename

        if cv2.imread(filepath) is None:
            print("Not an image file or corrupted file:")
            print(filepath)

        # if not filepath.endswith(".jpg") and not filepath.endswith("png"):
        #     print (filepath)