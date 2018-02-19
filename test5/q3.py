import sys
import os
def recursive(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                recursive(subfolder)
        print(folderName + ':')
        for filename in filenames:
            print '   ',filename 
root = sys.argv[1]
print root
recursive(root)

