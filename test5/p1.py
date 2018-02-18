import sys
import os
path = os.path.abspath(sys.argv[1][1:])
files = os.listdir(path)
for f in files:
        print(f)
