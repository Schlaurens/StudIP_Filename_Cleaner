import os
import re

os.remove("archive_filelist.csv")

for filename in os.listdir("."):
    os.rename(filename, re.sub('^[+[0-9]+]_', '', filename))
