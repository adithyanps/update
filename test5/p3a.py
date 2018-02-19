import sys
import os
def exe(path):
        print path
        files=os.listdir(path)
        for file in files:
         file=os.path.join(path,file)
         if os.path.isfile(file):
          print '  ',file
         else:
          exe(file)
          print file + ':'
rt = sys.argv[1]
print rt
exe(rt)

