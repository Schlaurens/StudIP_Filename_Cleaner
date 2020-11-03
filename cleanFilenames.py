import os
import re

#get the path of every file in every directory and subdirectory
for root, dirs, files in os.walk("."):
    for file in files: 

        if file == "archive_filelist.csv":
            os.remove(os.path.join(root, file))
            continue

        filename = os.path.join(root,file)

        #rename the files
        os.rename(filename, os.path.join(root, re.sub('^[+[0-9]+]_', '', file)))

print("Your files have been successfully cleansed!")