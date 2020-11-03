import os
import re

if os.path.isfile("archive_filelist.csv"):
    os.remove("archive_filelist.csv")

filelist = []

#get the path of every file in every directory and subdirectory
for root, dirs, files in os.walk("."):
    for file in files: 
        filename = os.path.join(root,file)
        #rename the files
        os.rename(filename, os.path.join(root, re.sub('^[+[0-9]+]_', '', file)))