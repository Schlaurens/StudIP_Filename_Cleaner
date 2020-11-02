import os
import re

for filename in os.listdir("."):
    os.rename(filename, re.sub('^[+[0-9]+]_', '', filename))


