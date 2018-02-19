import sys
import os
def exe(root,path):
	path = path + "/" + root
	if(os.path.isdir(path)):
		print path,":"
		print ""
	listFile = os.listdir(path)
	for f in listFile:
		print(f)
		if os.path.isdir(path + "/" + f):
			exe(f,path)
	path = path[:path.rfind("/")]
root = sys.argv[1]
print(root)
exe(root,os.getcwd())
