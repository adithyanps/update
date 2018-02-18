import sys
import os
path = os.path.abspath(sys.argv[1][1:])
files = os.listdir(path)
filesSize = []
for f in files:
	filePath = path + "/" + f
	if os.path.isfile(filePath):
		fileSet = (os.stat(filePath).st_size, f)
		filesSize.append(fileSet)
filesSize.sort(reverse = True)
for f in filesSize:
	print(f[1], "-", f[0])
