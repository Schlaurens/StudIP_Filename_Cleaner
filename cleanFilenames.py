import os
import re

if os.path.isfile("archive_filelist.csv"):
    os.remove("archive_filelist.csv")

filelist = []

#get the path of every file in every directory and subdirectory
for root, dirs, files in os.walk("."):
    for file in files: 
        filelist.append(os.path.join(root, file))
        
#rename the filenames
for filename in filelist: 
    os.rename(filename, os.path.join(os.path.dirname(filename), re.sub('^[+[0-9]+]_', '', os.path.basename(filename))))
