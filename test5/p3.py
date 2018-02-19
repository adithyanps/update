import sys
import os
def exe(root):
 print root

root = sys.argv[1]
root(exe)
path=os.listdir(root)
for f in path:
 if os.path.isfile(f):
   print f
 else:
  print f
  exe(root)
