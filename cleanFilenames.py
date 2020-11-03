import os
import re

if os.path.isfile("archive_filelist.csv"):
    os.remove("archive_filelist.csv")

for filename in os.listdir("."):
    os.rename(filename, re.sub('^[+[0-9]+]_', '', filename))
